import os
import requests
from django.shortcuts import render

def get_github_issues(request):
    url = "https://api.github.com/repos/DmBilyk/Bilyk.University.Online-Meditation-and-Mindfulness-Community/issues"
    headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Эта строка вызовет исключение для HTTP ошибок
        issues = response.json()
    except requests.exceptions.RequestException as e:
        # Обработайте исключение и передайте его в шаблон для отображения пользователю
        issues = []
        error_message = str(e)
        return render(request, 'issues/issues_list.html', {'issues': issues, 'error': error_message})
    return render(request, 'issues/issues_list.html', {'issues': issues})
