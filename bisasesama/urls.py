"""bisasesama URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import beranda.urls as beranda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('beranda.urls')),
    path('trigger_dua/', include('trigger_dua.urls', namespace='trigger_dua')),
    path('trigger_tiga/', include('trigger_tiga.urls', namespace='trigger_tiga')),
    path('pengguna/', include('pengguna.urls', namespace='pengguna')),
    path('trigger_empat/', include('trigger_empat.urls', namespace='trigger_empat')),
]
