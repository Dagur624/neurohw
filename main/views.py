from django.shortcuts import render
from . import models
def index(request):
    news = models.News.objects.all()
    return render(request, "index.html", {
        "news":news
    })
def lk(request):
    return render(request, "lk.html")
# Create your views here.
