from django.urls import path
from .views import HoraExtraList, HoraExtraUpdate, HoraExtraDelete, HoraExtraCreate

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horaextra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_horaextra'),
    path('editar/<int:pk>/', HoraExtraUpdate.as_view(), name='update_horaextra'),
    path('deletar/<int:pk>/', HoraExtraDelete.as_view(), name='delete_horaextra'),
]