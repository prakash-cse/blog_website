from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
    path("",views.home,name="home"),
    path("detail/<str:slug>",views.product_detail,name="product_detail"),
    path("old_url",views.old_url,name="old_func_url"),
    path("new_url_page001",views.new_url,name="new_page_url"),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about")
]