from django.urls import path
from .views import *

app_name = 'trigger_dua'

urlpatterns = [
    path("form_kategori/", form_kategori, name="form_kategori"),
    path("form_kategori/create_pasien", form_pasien, name="form_pasien"),
    path("form_kategori/cek_pasien", cek_pasien, name="cek_pasien"),
    path("form_kategori/create_rumah_ibadah", form_rumah_ibadah, name="form_rumah_ibadah"),
    path("form_kategori/cek_rumah_ibadah", cek_rumah_ibadah, name="cek_rumah_ibadah"),
    path("penggalangan_dana/", read_pdd_pribadi, name="read_pdd_pribadi"),
    path("penggalangan_dana/detail", read_pdd, name="read_pdd"),
    path("penggalangan_dana/create", form_penggalangan_dana, name="create_pdd"),
    path("penggalangan_dana/delete", delete_pdd, name="delete_komorbid"),
    path("komorbid/create/", create_komorbid, name="create_komorbid"),
    path("komorbid/update/", update_komorbid, name="update_komorbid"),
    path("komorbid/delete/", delete_komorbid, name="delete_komorbid"),
    path("komorbid/", read_komorbid, name="read_komorbid"),
]
