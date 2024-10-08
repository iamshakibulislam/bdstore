from django.shortcuts import render,HttpResponse,redirect
from .models import product
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.urls import reverse
from django.utils import timezone

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
                product.objects.create(title=title,price=float(price),description=description,image=image,user=request.user,created_at=timezone.now())
                messages.info(request,f"{title} - added successfully")
                return redirect("add_product")

            else:
                return HttpResponse("<h1>Invalid Data</h1>")
        
        except:
            messages.info(request,"Price should be in english number")
            return redirect("add_product")

        


def show_products(request):

    if request.method == "GET":
        keyword = request.GET.get("keyword")
        is_keyword = 0
        if keyword != None and len(keyword)>0 and keyword !="" and keyword != " ":
            is_keyword = 1

            product_list = product.objects.filter(user=request.user).filter(title__icontains=str(keyword)).order_by("id")[::-1]
        
        else:
            product_list = product.objects.filter(user=request.user).order_by("id")[::-1]
        page = Paginator(product_list,10)
        #started
        page_number = request.GET.get('page')
        try:
            page_obj = page.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = page.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = page.page(1)

        context = {'pages': page_obj,'count':len(page_obj),'is_keyword':is_keyword,"keyword":keyword}

        return render(request,"main/show_products.html",context)
    

def delete_product(request):
    get_product_id = request.GET.get('id')

    print("the product id is ",get_product_id)

    if get_product_id != None and get_product_id != "":
        sel_prod = product.objects.get(user=request.user,id=int(get_product_id))

        if sel_prod != None and sel_prod != "":
            sel_prod.delete()

            return JsonResponse({"status":"deleted"})
        
        else:
            return JsonResponse({"status":"error"})
    
    return JsonResponse({"status":"error"})



def edit_product(request):
    if request.method == "GET":
        get_id = request.GET.get('id')

        if get_id != None and get_id != "":
            sel_product= product.objects.get(user=request.user,id=int(get_id))
            return render(request,"main/edit_product.html",{"product_obj":sel_product})
        
    
    if request.method == "POST":

        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        prod_img = None
        id = request.POST.get('id')

        print("id is ",id)

        try:
            prod_img = request.FILES['product_image']
        except:
            prod_img = None

        sel_prod = product.objects.get(user=request.user,id=int(id))

        sel_prod.title = title
        sel_prod.price = float(price)
        sel_prod.description = description

        if prod_img != None and prod_img != "":
            sel_prod.image = prod_img
        
        sel_prod.save()

        messages.info(request,"Product updated successfully ")

        reversed_url = reverse('edit_product')

        return redirect(f"{reversed_url}?id={id}")