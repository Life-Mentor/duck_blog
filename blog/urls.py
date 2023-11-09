from django.urls import path
from .views import *

urlpatterns = [
    path('',index.as_view(),name="index"),
    path('qq/',qq,name='qq'),
    path('wen/',wenz,name='wen'),
]
