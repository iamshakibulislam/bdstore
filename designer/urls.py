from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name="editor"),
    path('pages',views.pages,name="pages"),
    path('add_landing_page',views.add_landing_page,name="add_landing_page")
]