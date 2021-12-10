from django.db import connection
from django.shortcuts import render, redirect
from pengguna.forms import *

def cursor_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def pengguna(function):
    def wrapper(request, *args, **kwargs):
        email = request.session.get('email')
        if email is None:
            return redirect('/login/')
        else:
            return function(request, *args, **kwargs)
    return wrapper

def tidak_ada_pengguna (function):
    def wrapper(request, *args, **kwargs):
        email = request.session.get('email')
        if email is not None:
            return redirect('/profile_pengguna/')
        else:
            return function(request, *args, **kwargs)
    return wrapper

def cek_role(email):
    with connection.cursor() as cursor:
        for i in ["ADMIN", "PENGGALANG_DANA", "INDIVIDU", "ORGANISASI"]:
            cursor.execute(
                f"SELECT * FROM {i} WHERE email=%s LIMIT 1;",
                [email])
            if cursor.fetchone() is not None:
                return i

def dapatkan_role(email, role):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT * FROM {role} WHERE email=%s LIMIT 1;",
            [email])
        return cursor.fetchone()

def input_session(request, email, nama):
    request.session['email'] = email
    request.session['nama'] = nama
    request.session['role'] = dapatkan_role(email)


@tidak_ada_pengguna
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM PENGGALANG_DANA WHERE email=%s LIMIT 1;",
                    [form.cleaned_data.get('email')])
                data = cursor.fetchone()
            input_session(request, form.cleaned_data.get('email'), data[3])
            return redirect('/profile_pengguna/')
    elif request.method == 'GET':
        form = LoginForm()
    context = {'form': form}
    return render(request, "login.html", context)

@tidak_ada_pengguna
def register(request):
    if request.method == 'POST':
        form = PilihRoleForm(request.POST)
        if form.is_valid():
            alamat_url = {'ADMIN': '/admin/',
                       'PENGGALANG_DANA': '/penggalang_dana/',
                       'INDIVIDU': '/penggalang_dana/individu/',
                       'ORGANISASI': '/penggalang_dana/organisasi/'}
            return redirect(alamat_url[form.cleaned_data.get('peran')])
    elif request.method == 'GET':
        form = PilihRoleForm()
    context = {'form': form}
    return render(request, 'register_role.html', context)

@tidak_ada_pengguna
def form_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            nama = form.cleaned_data.get('nama')
            input_session(request, form.cleaned_data.get('email'), nama)
            return redirect('/profile_pengguna/')
    elif request.method == 'GET':
        form = AdminForm()
    context = {'form': form}
    return render(request, 'form_admin.html', context)

@tidak_ada_pengguna
def form_pd(request):
    if request.method == 'POST':
        form = PenggalangDanaForm(request.POST)
        if form.is_valid():
            form.save()
            nama = form.cleaned_data.get('nama')
            input_session(request, form.cleaned_data.get('email'), nama)
            return redirect('/profile_pengguna/')
    elif request.method == 'GET':
        form = PenggalangDanaForm()
    context = {'form': form}
    return render(request, 'form_penggalang_dana.html', context)

@tidak_ada_pengguna
def form_pd_individu(request):
    if request.method == 'POST':
        form = IndividuForm(request.POST)
        if form.is_valid():
            form.save()
            nama = form.cleaned_data.get('nama')
            input_session(request, form.cleaned_data.get('email'), nama)
            return redirect('/profile_pengguna/')
    elif request.method == 'GET':
        form = IndividuForm()
    context = {'form': form}
    return render(request, 'form_pd_individu.html', context)

@tidak_ada_pengguna
def form_pd_organisasi(request):
    if request.method == 'POST':
        form = OrganisasiForm(request.POST)
        if form.is_valid():
            form.save()
            nama = form.cleaned_data.get('nama')
            input_session(request, form.cleaned_data.get('email'), nama)
            return redirect('/profile_pengguna/')
    elif request.method == 'GET':
        form = OrganisasiForm()
    context = {'form': form}
    return render(request, 'form_pd_organisasi.html', context)

@pengguna
def profil_pengguna(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM PENGGALANG_DANA WHERE email=%s",
                       [request.session.get("email")])
        data_pengguna = cursor.fetchone()
        role_pengguna = dapatkan_role(
            request.session.get("email"),
            request.session.get("role"))
    context = {'user': data_pengguna, 'role': role_pengguna}
    return render(request, 'profil_pengguna.html', context)

@pengguna
def profil_pengguna_individu_adminview(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM INDIVIDU WHERE email=%s",
                       [request.session.get("email")])
        data_pengguna = cursor.fetchone()
        role_pengguna = dapatkan_role(
            request.session.get("email"),
            request.session.get("role"))
    context = {'user': data_pengguna, 'role': role_pengguna}
    return render(request, 'profil_pengguna_individu_adminview.html')

@pengguna
def profil_pengguna_organisasi_adminview(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM ORGANISASI WHERE email=%s",
                       [request.session.get("email")])
        data_pengguna = cursor.fetchone()
        role_pengguna = dapatkan_role(
            request.session.get("email"),
            request.session.get("role"))
    context = {'user': data_pengguna, 'role': role_pengguna}
    return render(request, 'profil_pengguna_organisasi_adminview.html')

# Admin only page. Pengguna cannot access
@pengguna
def read_daftar_pengguna_admin(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT email, nama, jenis, status_verifikasi FROM PENGGALANG_DANA;")
        data_pengguna = cursor_fetchall(cursor)
    context = {'data': data_pengguna}
    return render(request, 'read_daftar_pengguna_admin.html')

@pengguna
def read_daftar_pengguna_admin_afterverif(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT email, nama, jenis, status_verifikasi "
                       "FROM PENGGALANG_DANA "
                       "WHERE status_verifikasi = 'VERIFIED';")
        data_pengguna= cursor_fetchall(cursor)
    context = {'data': data_pengguna}
    return render(request, 'read_daftar_pengguna_admin_afterverif.html')
