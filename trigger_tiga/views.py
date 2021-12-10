from django.shortcuts import render

from pengguna.views import admin

@admin
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

# Halaman kategori penggalangan dana
# Hanya dapat diakses oleh admin => Soalnya ada Update button nya
def read_kategori_penggalangan_dana_admin(request):
    return render(request, 'read_kategori_penggalangan_dana_admin.html')

def form_create_kategori_penggalangan_dana(request):
    return render(request, 'form_create_kategori_penggalangan_dana.html')

def form_update_kategori_penggalangan_dana(request):
    return render(request, 'form_update_kategori_penggalangan_dana.html')

