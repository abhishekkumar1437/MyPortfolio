from django.contrib import admin
from django.urls import path,include
from . import views




urlpatterns = [
     path('',views.portfolio, name='portfolio'),
     path('Contact',views.Contact,name='Contact'),
    

]
