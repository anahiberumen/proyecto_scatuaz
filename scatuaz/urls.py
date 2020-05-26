from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trabajador/', include('trabajador.urls')),
    path('usuario/', include('usuario.urls')),
    path('', include('login.urls')),
]
