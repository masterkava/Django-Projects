#i have created this file - Mayur
from django. http import HttpResponse
from django.shortcuts import render
def index(request):
    dicti= {'name':'mike', 'place':'india'}
    return render(request, 'index.html', dicti)

def capitalizefirst(request):
    return HttpResponse('capitalizefirst <a href="/">Back</a>')

def removepunc(request):
    return HttpResponse('removepunc')

def newlineremove(request):
    return HttpResponse('newlineremove')

def spaceremove(request):
    return HttpResponse('spaceremove')

def charcount(request):
    return HttpResponse('charcount')


