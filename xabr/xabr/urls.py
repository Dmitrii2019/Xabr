from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainapp.urls', namespace='main')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('blog/', include('blogapp.urls', namespace='blogapp')),
    path('admin/', admin.site.urls),
]
