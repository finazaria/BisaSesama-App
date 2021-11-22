from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    path("", login, name="login"),

]
    # path("form_donasi/", form_donasi, name="form_donasi"),
    # path("donasi/read_donasi", read_donasi, name="read_donasi"),
    # path("donasi/read_detail_donasi", read_detail_donasi, name="read_detail_donasi"),