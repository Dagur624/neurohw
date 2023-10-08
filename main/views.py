from django.shortcuts import render
from . import models
def index(request):
    news = models.News.objects.all()
    return render(request, "index.html", {
        "news":news
    })
# Create your views here.
