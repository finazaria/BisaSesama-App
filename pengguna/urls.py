from django.urls import path
from .views import *

app_name = 'pengguna'

urlpatterns = [
    path("admin", form_admin, name="admin"),
    path("penggalang_dana", form_pd, name="penggalang_dana"),
    path("penggalang_dana/individu", form_pd_individu, name="pd_individu"),
    path("penggalang_dana/organisasi", form_pd_organisasi, name="pd_organisasi"),

]
