from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view.as_view(),name='login'),
    path("reirster/",reirster.as_view(),name="reirster"),
    path('active/<active_code>',active_user,name='active'),
    path('forget/',forget_pwd.as_view(),name='forget'),
    path('reset/<active_code>',reset_pwd.as_view(),name='reset'),
    path('home/',user_home,name='home'),
    path('logout/',logout_user,name='logout')
]
