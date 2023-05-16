from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return render(request, '')

def categories(request, catid):
    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Categories</h1><p1>{catid}</p1>")

def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Archive by year</h1><p1>{year}</p1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found</h1>")
