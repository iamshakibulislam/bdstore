from django.contrib import admin
from .models import *


admin.site.register(domains)
admin.site.register(domain_path)
admin.site.register(prebuilt_pages)