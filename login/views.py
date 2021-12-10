from django.db import connection
from django.shortcuts import render, redirect
from login.forms import LoginForm
from django.contrib import messages

def no_user(function):
    def wrapper(request, *args, **kwargs):
        email = request.session.get('email')
        if email is not None:
            return redirect('/profile/')
        else:
            return function(request, *args, **kwargs)
    return wrapper

def login(request):
    email = None
    nama = None
    role = None
    role_pdd = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            with connection.cursor() as cursor:
                cursor.execute('set search_path to tk_sidona')
                for i in ['ADMIN', 'PENGGALANG_DANA']:
                    cursor.execute(
                        f"SELECT * FROM {i} WHERE email=%s LIMIT 1;",
                        [form.cleaned_data.get('email')])
                    data = cursor.fetchone()
                    print(data)
                    if data is not None:
                        email = form.cleaned_data.get('email')
                        nama = data[2]
                        role = i
                        break
                if data is None or form.cleaned_data.get('password') != data[1]:
                    messages.add_message(request, messages.WARNING,
                                         f"Maaf, email atau password yang Anda masukkan salah")
                    context = {'form': form}
                    return render(request, "login.html", context)

                if role == 'PENGGALANG_DANA':
                    for i in ['INDIVIDU', 'ORGANISASI']:
                        cursor.execute(
                            f"SELECT * FROM {i} WHERE email=%s LIMIT 1;",
                            [form.cleaned_data.get('email')])
                        data_pdd = cursor.fetchone()
                        if data_pdd is not None:
                            role_pdd = i
                cursor.execute('set search_path to public')
                request.session["email"] = email
                request.session["nama"] = nama
                request.session["role"] = role
                request.session["role_pdd"] = role_pdd
            return redirect('')
    elif request.method == 'GET':
        form = LoginForm()
    context = {'form': form}
    return render(request, "login.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')
