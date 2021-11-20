from django.shortcuts import render

def form_kategori(request):
    return render(request, 'create_kategori_penggalangan_dana.html')

def form_pasien(request):
    return render(request, 'create_form_pasien.html')

def cek_pasien(request):
    return render(request, 'cek_pasien_terdaftar.html')

def form_rumah_ibadah(request):
    return render(request, 'create_form_rumah_ibadah.html')

def cek_rumah_ibadah(request):
    return render(request, 'cek_rumah_ibadah_terdaftar.html')

def form_penggalangan_dana(request):
    return render(request, 'create_form_penggalangan_dana.html')

def read_pdd_pribadi(request):
    return render(request, 'read_penggalangan_dana_pribadi.html')

def read_pdd(request):
    return render(request, 'read_penggalangan_dana.html')

def delete_pdd(request):
    return render(request, 'read_penggalangan_dana_pribadi.html')

def cairkan_pdd(request):
    return render(request, 'read_penggalangan_dana_pribadi.html')

def read_komorbid(request):
    return render(request, 'read_komorbid.html')

def create_komorbid(request):
    return render(request, 'create_komorbid.html')

def update_komorbid(request):
    return render(request, 'update_komorbid.html')

def delete_komorbid(request):
    return render(request, 'read_komorbid.html')