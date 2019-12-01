from django.shortcuts import render
from django.http import JsonResponse
import platform
from datetime import datetime


def main(request):
    return render(request, 'main.html', {'parameter': "test"})


def health(request):
    response = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'current_page': request.path,
        'server_info': {
            'System' : platform.system(),
            'Release': platform.release(),
            'Type'   : platform.machine()
        },
        'client_info': request.META['HTTP_USER_AGENT']
    }
    return JsonResponse(response)