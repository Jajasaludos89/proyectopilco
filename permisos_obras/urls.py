from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

def inicio(request):
    return redirect('lista_autorizaciones')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autorizaciones/', include('autorizaciones.urls')),
    path('', inicio, name='inicio'),  # Redirige la raíz a autorizaciones
]
