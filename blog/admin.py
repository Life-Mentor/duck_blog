from django.contrib import admin
# from django.contrib.auth.models import User
from .models import *

admin.site.register(Catgory)
admin.site.register(Tag)
admin.site.register(Post)


