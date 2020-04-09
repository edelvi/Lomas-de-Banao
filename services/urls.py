from django.conf.urls import url
from django.urls import path

from . import views
from services.views import index, about, prices

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('prices', views.prices, name="prices"),
    path('specialists', views.specialists, name="specialists"),
    path('gallery', views.gallery, name="gallery"),
    path('contact', views.contact, name="contact")
]
