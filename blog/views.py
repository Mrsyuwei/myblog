from django.shortcuts import render
from django.http import HttpResponse
import models


def index(request):
    return HttpResponse('hello world!')


def baby(request):
    return render(request, 'index.html', {'ok': 'hello a yu baby!'})


def homepage(request):
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def articlepage(request, page_id):
    article = models.Article.objects.get(pk=page_id)
    return render(request, 'article.html', {'article': article})

def edit_action(request,page_id):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    if page_id=='0':
        models.Article.objects.create(Title=title,Content=content)
    else:
        models.Article.objects.filter(pk=page_id).update(Title=title,Content=content)
    articles=models.Article.objects.all()
    return render(request,'index.html',{'articles': articles})

def edit_page(request):
    return render(request,'edit.html')

def rechange(request,page_id):
    article=models.Article.objects.get(pk=page_id)
    return render(request,'rechange.html',{"article":article})

# Create your views here.
