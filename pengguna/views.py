from django.shortcuts import render

def form_admin(request):
    return render(request, 'form_admin.html')

def form_pd(request):
    return render(request, 'form_penggalang_dana.html')

def form_pd_individu(request):
    return render(request, 'form_pd_individu.html')

def form_pd_organisasi(request):
    return render(request, 'form_pd_organisasi.html')