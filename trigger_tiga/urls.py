from django.urls import path
from .views import *

app_name = 'trigger_tiga'

urlpatterns = [
    path("daftar-penggalangan-dana-admin", read_daftar_penggalangan_dana_admin, name="daftar-penggalangan-dana-admin"),
    path("daftar-afterverif-penggalangan-dana-admin", read_afterverif_penggalangan_dana_admin, name="daftar-afterverif-penggalangan-dana-admin"),
    path("detail1-daftar-penggalangan-dana", detail1_daftar_penggalangan_dana, name="detail1-daftar-penggalangan-dana"),
    path("detail2-daftar-penggalangan-dana", detail2_daftar_penggalangan_dana, name="detail2-daftar-penggalangan-dana"),
    path("update-penggalangan-dana", form_update_penggalangan_dana, name="form-update-penggalangan-dana"),
    path("form-verifikasi-penggalangan-dana", form_verifikasi_penggalangan_dana, name="form-verifikasi-penggalangan-dana"),

    
]
