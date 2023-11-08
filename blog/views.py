from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *

class index(View):
    def get(self,request):
        catgorys = Catgory.objects.all()
        post_list = Post.objects.all()
        return render(request,"index/index.html",{'catgorys':catgorys,'post_list':post_list})


