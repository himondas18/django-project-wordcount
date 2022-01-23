# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
def himon(request):
    return HttpResponse('<h1>Hello</h1>')
def count(request):
    fulltext = request.GET['fulltext']
    wordcount = len(fulltext.split())
    #print(wordcount)
    worddic = {"himon":2,"Das":1}
    worddic = sorted(worddic.items(), reverse = False)
    return render(request, 'count.html',{'fulltext':fulltext,'Wordcount':str(wordcount), 'worddic':worddic})
def about(request):
    return render(request, 'about.html')