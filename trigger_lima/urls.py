from django.urls import path
from .views import *

app_name = 'trigger_lima'

urlpatterns = [
    path('form_pencairan_dana/', form_pencairan_dana, name='form_pencairan_dana'),
]