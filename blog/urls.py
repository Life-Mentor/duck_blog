from django.urls import path
from .views import *

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('ce/',ceshi,name='ce'),
]
