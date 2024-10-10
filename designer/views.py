from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"designer/index.html")



def pages(request):

    if request.method == "GET":
        return render(request,"main/landing_pages.html")
    


def add_landing_page(request):

    if request.method == "GET":
        return render(request,"main/add_landing_page.html")