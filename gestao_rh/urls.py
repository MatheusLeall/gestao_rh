from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.core.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('hora-extra/', include('apps.registro_hora_extra.urls')),
    path('admin', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
