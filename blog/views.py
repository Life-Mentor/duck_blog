from django.shortcuts import render, HttpResponse
from django.views import View

class index(View):
    def get(self,request):
        return render(request,"index.html")

