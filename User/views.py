from django.shortcuts import render,redirect
from django.contrib import auth
from .models import User
from django.contrib import messages

from designer.models import domains

def registration(request):
    if request.method == 'GET':
        return render(request,"main/pages/samples/register.html")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if email != None and email != "" and len(email) > 0 and password != None and len(password) != 0:
            try:
                chk=User.objects.filter(email = email)
                if len(chk) > 0:
                    messages.info(request,"User already exists!")
                    return redirect("registration")
                    
                User.objects.create_user(email=email,password = password)
                
                user_auth = auth.authenticate(email=email,password=password)


                auth.login(request,user_auth)

                split_email = email.split("@")[0]

                main_domain = "mydomain.com"

                sub_domain = split_email+f".{main_domain}"

                check_domain = domains.objects.filter(domain=split_email+f".{main_domain}")

                if len(check_domain) > 0:
                    sub_domain = split_email+str(request.user.id)+str(check_domain[0].id)+f".{main_domain}"

                domains.objects.create(user=request.user,domain = sub_domain)

                return redirect("dashboard")
            except:
                messages.info(request,"Registration failed!")
                return redirect("registration")
        else:
            messages.info(request,"Email aor Password can not be blank!")
            return redirect("registration")

    

def login(request):
    if request.method == "GET":
        return render(request,"main/pages/samples/login.html")
    
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email != None and password != None:
            try:
                user_auth = auth.authenticate(email=email,password=password)
                

                if user_auth is not None:
                    auth.login(request,user_auth)
                    return redirect("dashboard")
                else:
                    messages.info(request,"Email Or Password Is Incorrect")
                    return redirect("login")

            except:
                messages.info(request,"Email Or Password Is Incorrect")
                return redirect("login")


def logout(request):
    auth.logout(request)
    return redirect('home_page')


