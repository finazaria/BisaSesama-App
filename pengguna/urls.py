from django.urls import path
from .views import *

app_name = 'pengguna'

urlpatterns = [
    path("admin", form_admin, name="admin"),
    path("penggalang_dana", form_pd, name="penggalang_dana"),
    path("penggalang_dana/individu", form_pd_individu, name="pd_individu"),
    path("penggalang_dana/organisasi", form_pd_organisasi, name="pd_organisasi"),
    path("profil_pengguna", profil_pengguna, name="profil-pengguna"),
    path("daftar-pengguna-admin", read_daftar_pengguna_admin, name="daftar-pengguna-admin"),
    path("daftar-pengguna-admin-afterverif", read_daftar_pengguna_admin_afterverif, name="daftar-pengguna-admin-afterverif"),
    path("profil-pengguna-individu-adminview", profil_pengguna_individu_adminview, name="profil-pengguna-individu-adminview"),
    path("profil-pengguna-organisasi-adminview", profil_pengguna_organisasi_adminview, name="profil-pengguna-organisasi-adminview"),
    


]
