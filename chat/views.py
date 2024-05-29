import os
import openai
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from datetime import timedelta

openai.api_key = settings.LEPTON_API_TOKEN

VALID_KEYWORDS = ['meditation', 'mindfulness', 'zen', 'relaxation', 'breathing', 'yoga']

def chat_page(request):
    return render(request, 'chat/chat_page.html')

@csrf_exempt
def get_openai_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        user_ip = get_client_ip(request)

        if not any(keyword in user_message.lower() for keyword in VALID_KEYWORDS):
            return JsonResponse({'response': 'Please ask questions related to meditation.'})

        if not rate_limit_check(user_ip):
            return JsonResponse({'response': 'Rate limit exceeded. Please wait before making more requests.'})

        client = openai.OpenAI(
            base_url="https://openchat-3-5.lepton.run/api/v1/",
            api_key=openai.api_key
        )

        completion = client.chat.completions.create(
            model="openchat-3-5",
            messages=[
                {"role": "user", "content": user_message},
            ],
            max_tokens=128,
            stream=True,
        )

        response_text = ""
        for chunk in completion:
            if not chunk.choices:
                continue
            content = chunk.choices[0].delta.content
            if content:
                response_text += content

        return JsonResponse({'response': response_text})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def rate_limit_check(user_ip):
    cache_key = f"rate_limit_{user_ip}"
    requests = cache.get(cache_key, 0)

    if requests >= 10:
        return False

    cache.set(cache_key, requests + 1, timeout=3600)
    return True
