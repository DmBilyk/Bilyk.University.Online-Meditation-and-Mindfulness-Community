import requests
from django.shortcuts import render
from rest_framework.views import APIView

class HttpCatView(APIView):
    def get(self, request, status_code):
        url = f'https://http.cat/{status_code}'
        response = requests.get(url)
        if response.status_code == 200:
            return render(request, 'cats/httpcat.html', {'status_code': status_code, 'url': url})
        return render(request, 'cats/httpcat.html', {'error': 'Invalid status code'})
