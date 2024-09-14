from django.shortcuts import render,HttpResponse,redirect
from .models import product
from django.contrib import messages

def add_product(request):
    if request.method == "GET":
        return render(request,"main/add_product.html")
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image = request.FILES["product_image"]

        try:

            if len(title)>0 and float(price) > 0 and len(description)>0:
                product.objects.create(title=title,price=float(price),description=description,image=image,user=request.user)
                messages.info(request,f"{title} - added successfully")
                return redirect("add_product")

            else:
                return HttpResponse("<h1>Invalid Data</h1>")
        
        except:
            messages.info(request,"Price should be in english number")
            return redirect("add_product")

        

