from django.urls import path
from .views import *

app_name = 'trigger_tiga'

urlpatterns = [
    path("daftar-penggalangan-dana-admin", read_daftar_penggalangan_dana_admin, name="daftar-penggalangan-dana-admin"),
    
]
