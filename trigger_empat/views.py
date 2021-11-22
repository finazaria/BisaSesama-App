from django.shortcuts import render

# Create your views here.


def cek_penggalangan_dana(request):
    return render(request, 'read_data_donasi_penggalangan_danaPOVPENGGUNA.html')

def form_donasi(request):
    return render(request, 'create_form_pembuatan_donasi.html')

def read_donasi(request):
    return render(request, 'read_data_donasi_penggalangan_dana.html')

def read_detail_donasi(request):
    return render(request,'read_detail_donasi.html' )