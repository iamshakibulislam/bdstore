from django.db import models
from User.models import User

class product(models.Model):
    user = models.ForeignKey(User,default=3,on_delete=models.CASCADE)
    title = models.CharField(max_length=400,null=False,blank=False)
    price = models.FloatField(default=0)
    description = models.TextField(default="product description")
    image = models.ImageField(upload_to="product_images")


    def __str__(self):
        return str(self.title)
