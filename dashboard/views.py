from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request,"main/index.html")



def handle_domain_request(domain_host, path_after_first_slash):
    # Process the captured domain and path as needed
    # For demonstration, we'll just return a simple response

    # Here you can implement your custom logic
    response_text = f"Domain: {domain_host}, Path: {path_after_first_slash}"
    return HttpResponse(response_text)