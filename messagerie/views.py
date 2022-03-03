from django.shortcuts import render
from django.http import HttpResponse

def messagerie(request):
    return render(request, 'messagerie/chat.html')
