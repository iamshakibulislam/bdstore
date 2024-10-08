# myapp/middleware.py
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from .views import handle_domain_request  # Import your view function

class DomainCaptureMiddleware(MiddlewareMixin):
    """
    Middleware to capture the domain host and the URL path after the first '/'.
    """

    def process_request(self, request):
        # Capture the domain host
        domain_host = request.get_host()

        if domain_host == "127.0.0.1:8000":
            return None
        
        # Capture the path after the first '/'
        path_after_first_slash = request.path.lstrip('/')  # Removes the leading '/'
        
        # Call the view function and pass the captured data
        response = handle_domain_request(domain_host, path_after_first_slash)
        
        return response  # Return the response from the view function
