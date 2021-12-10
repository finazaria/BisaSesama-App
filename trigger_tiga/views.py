from django.db import connection
from django.shortcuts import render

from pengguna.views import admin

with connection.cursor() as cursor:
        cursor.execute(
            """
            SET SEARCH_PATH TO TK_SIDONA;
            """
        )

@admin
def read_daftar_penggalangan_dana_admin(request):
    context = {}
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM PENGGALANGAN_DANA_PD;
            """
        )
        
        data = cursor.fetchall()
        print(data)

        context['data_pd'] = data
    return render(request, 'read_daftar_penggalangan_dana_admin.html', context)

def read_afterverif_penggalangan_dana_admin(request):
    return render(request, 'read_afterverif_daftar_penggalangan_dana_admin.html')

def detail1_daftar_penggalangan_dana(request):
    return render(request, 'detail1_daftar_penggalangan_dana_admin.html')

def detail2_daftar_penggalangan_dana(request):
    return render(request, 'detail2_daftar_penggalangan_dana_admin.html')

# POV Pengguna
def form_update_penggalangan_dana(request):
    id_verifikasi=request.session.get("verifikasi_id")
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

