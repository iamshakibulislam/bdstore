from django.db import models
from User.models import User
from products.models import *

class domains(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    domain = models.CharField(max_length=100,null=True)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return str(self.domain)
    


class domain_path(models.Model):
    domain = models.ForeignKey(domains,on_delete=models.CASCADE)
    path = models.CharField(max_length=400,null=True)


    def __str__(self):
        if self.path == None or self.path == "":
            return str(self.domain)
        return str(self.domain)+"/"+str(self.path)
    


class landing_page(models.Model):
    name = models.CharField(max_length=400)
    url_path = models.ForeignKey(domain_path,on_delete=models.CASCADE)
    landing_source = models.TextField(null=False)
    product = models.ForeignKey(product,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.name)


class prebuilt_pages(models.Model):

    name = models.CharField(max_length=255)
    source = models.TextField(null=False)

    def __str__(self):
        return str(self.name)