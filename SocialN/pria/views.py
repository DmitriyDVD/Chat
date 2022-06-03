from django.shortcuts import render


def index(request):
    return render(request, 'pria/zaglav.html')

def mypage(request):
    return render(request, 'pria/mypage.html')

def messenger(request):
    return render(request, 'pria/messenger.html')

def chat(request):
    return render(request, 'pria/chat.py')    