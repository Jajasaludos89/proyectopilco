from django.urls import path
from .views import lista_autorizaciones, crear_autorizacion, editar_autorizacion, eliminar_autorizacion
from .views import lista_proyectos, crear_proyecto, editar_proyecto, aprobar_proyecto, eliminar_proyecto
from .views import lista_municipios, crear_municipio, editar_municipio, eliminar_municipio
from .views import lista_condiciones, crear_condicion, editar_condicion, eliminar_condicion

urlpatterns = [
    # Rutas para Autorizaciones
    path('', lista_autorizaciones, name='lista_autorizaciones'),
    path('nuevo/', crear_autorizacion, name='crear_autorizacion'),
    path('editar/<int:pk>/', editar_autorizacion, name='editar_autorizacion'),
    path('eliminar/<int:pk>/', eliminar_autorizacion, name='eliminar_autorizacion'),

    # Rutas para Proyectos
    path('proyectos/', lista_proyectos, name='lista_proyectos'),
    path('proyectos/nuevo/', crear_proyecto, name='crear_proyecto'),
    path('proyectos/editar/<int:pk>/', editar_proyecto, name='editar_proyecto'),
    path('proyectos/aprobar/<int:pk>/', aprobar_proyecto, name='aprobar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', eliminar_proyecto, name='eliminar_proyecto'),
    
    # Rutas para Municipios
    path('municipios/', lista_municipios, name='lista_municipios'),
    path('municipios/nuevo/', crear_municipio, name='crear_municipio'),
    path('municipios/editar/<int:pk>/', editar_municipio, name='editar_municipio'),
    path('municipios/eliminar/<int:pk>/', eliminar_municipio, name='eliminar_municipio'),

  
    path('condiciones/', lista_condiciones, name='lista_condiciones'),
    path('condiciones/nuevo/', crear_condicion, name='crear_condicion'),
    path('condiciones/editar/<int:pk>/', editar_condicion, name='editar_condicion'),
    path('condiciones/eliminar/<int:pk>/', eliminar_condicion, name='eliminar_condicion'),
] 
