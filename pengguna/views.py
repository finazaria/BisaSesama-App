from django.shortcuts import render

def register(request):
    return render(request, 'register_role.html')

def form_admin(request):
    return render(request, 'form_admin.html')

def form_pd(request):
    return render(request, 'form_penggalang_dana.html')

def form_pd_individu(request):
    return render(request, 'form_pd_individu.html')

def form_pd_organisasi(request):
    return render(request, 'form_pd_organisasi.html')

def profil_pengguna(request):
    return render(request, 'profil_pengguna.html')

# Admin only page. Pengguna cannot access
def read_daftar_pengguna_admin(request):
    return render(request, 'read_daftar_pengguna_admin.html')

def read_daftar_pengguna_admin_afterverif(request):
    return render(request, 'read_daftar_pengguna_admin_afterverif.html')

def profil_pengguna_individu_adminview(request):
    return render(request, 'profil_pengguna_individu_adminview.html')

def profil_pengguna_organisasi_adminview(request):
    return render(request, 'profil_pengguna_organisasi_adminview.html')
