from django.http import HttpResponse
from article.models import Articles
from django.shortcuts import render
import random

def index(request):
    article_list = Articles.objects.all().order_by('publication_date')[:10]
    context = {}

    if article_list:
        list_len = len(article_list)

        rand = random.randint(0, list_len - 1)
        context = {'article_list': article_list,
                   'random_article': article_list[rand],
                   'length': list_len
                   }
        return render(request, "article/home.html", context)
    else:
        return HttpResponse("No article found")

def detail(request, id):

    context = {}
    article = Articles.objects.get(id = id)
    article_list = Articles.objects.all()[:5]
    if article:
        return render(request, "article/detail.html", {'article':article, 'article_list':article_list})
    else:
        return HttpResponse("No article found")