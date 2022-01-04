from django.urls import path
from .views import *

urlpatterns = [
    path('lihat/<int:id>',user_lihat,name='user_lihat'),
    path('',users, name='tabel_users'),
    path('edit/<str:id>',user_edit, name='user_edit'),
    path('delete/<str:id>',user_delete, name='user_delete'),
]
