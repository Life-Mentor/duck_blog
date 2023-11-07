from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("blog.urls","blog"),namespace="blog")),
    path('users/', include(("users.urls","blog"),namespace="users")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # 配置静态文件url

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
