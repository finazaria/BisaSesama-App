from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def read_daftar_penggalangan_dana_admin(request):
    return render(request, 'read_daftar_penggalangan_dana_admin.html')

def read_afterverif_penggalangan_dana_admin(request):
    return render(request, 'read_afterverif_daftar_penggalangan_dana_admin.html')

def detail1_daftar_penggalangan_dana(request):
    return render(request, 'detail1_daftar_penggalangan_dana_admin.html')

def detail2_daftar_penggalangan_dana(request):
    return render(request, 'detail2_daftar_penggalangan_dana_admin.html')

# POV Pengguna
def form_update_penggalangan_dana(request):
    return render(request, 'form_update_penggalangan_dana.html')

# Catatan pengajuan
# Hanya boleh dilakukan admin
def form_verifikasi_penggalangan_dana(request):
    return render(request, 'form_verifikasi_penggalangan_dana.html')

