from django.shortcuts import render
from . import models
def index(request):
    news = models.News.objects.all()
    return render(request, "index.html", {
        "news":news
    })
def lk(request):
    if request.user.user_type.code == 'student':
        return render(request, "lk1.html")
    elif request.user.user_type.code == 'teacher':

        return render(request, "lk.html")
# Create your views here.
