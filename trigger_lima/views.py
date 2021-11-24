from django.shortcuts import render

# Create your views here.

def form_pencairan_dana(request):
    return render(request, 'create_form_pencairan_dana.html')

def data_penggalang_dana(request):
    return render(request, 'profil')