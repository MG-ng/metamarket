from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, "app_metamarkt/index.html")


def search(request):
    if request.method == "GET":
        search_phrase = request.GET.get('q', None)
        if search_phrase:
            pass
        return render(request, "app_metamarkt/search.html", {"search_phrase": search_phrase})


