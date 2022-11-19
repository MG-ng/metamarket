from django.shortcuts import render
from django.views import generic


def index(request):
    if request.method == "POST":
        pass
    elif request.method == "GET":
        return render(request, "app_metamarkt/index.html")


