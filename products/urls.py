from django.urls import path
from . import views

urlpatterns = [
    path('add_product', views.add_product,name="add_product"),
    path('show_products',views.show_products,name="show_products"),
    path('delete_product',views.delete_product,name="delete_product"),
    path('edit_product',views.edit_product,name='edit_product'),
    
]
