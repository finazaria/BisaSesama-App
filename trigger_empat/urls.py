from django.urls import path
from .views import *

app_name = 'trigger_empat'

urlpatterns = [
    path("penggalangan_dana_POV_Pengguna/", cek_penggalangan_dana, name="read_halaman_penggalangan_dana"),
    path("form_donasi/", form_donasi, name="form_donasi"),
    path("donasi/read_donasi", read_donasi, name="read_donasi"),
    path("donasi/read_detail_donasi", read_detail_donasi, name="read_detail_donasi"),
    # path("form_kategori/create_rumah_ibadah", form_rumah_ibadah, name="form_rumah_ibadah"),
    # path("form_kategori/cek_rumah_ibadah", cek_rumah_ibadah, name="cek_rumah_ibadah"),
    # path("penggalangan_dana/", read_pdd_pribadi, name="read_pdd_pribadi"),  
]