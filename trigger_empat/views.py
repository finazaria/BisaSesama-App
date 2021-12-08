from decimal import Context
from django.shortcuts import redirect, render
from django.db import connection

from pengguna.views import pengguna, cursor_fetchall
from .forms import *
import datetime

# Create your views here.

@pengguna
def cek_penggalangan_dana(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT *"
                       "FROM PENGGALANGAN_DANA_PD"
                      ";")
        data_pengguna= cursor_fetchall(cursor)
    context = {'data': data_pengguna}
    return render(request, 'read_data_donasi_penggalangan_danaPOVPENGGUNA.html', context)
# @pengguna
def form_donasi(request):
    # with connection.cursor() as cursor:
    if request.method == 'POST':
        form = Tambah_Donasi(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("pengguna : read_detail_donasi")
    elif request.method == 'GET':
        if request.GET.get('id_d') is None:
            return redirect("pengguna : read_halaman_penggalangan_dana")
        with connection.cursor() as cursor:
            cursor.execute("SET SEARCH_PATH TO SIDONA SELECT id, judul FROM PENGGALANGAN_DANA_PD WHERE id = %s LIMIT 1;", [request.GET.get('id_d')])
            data = cursor.fetchone()
            judul = data[1]
            timestamp = datetime.datetime.now()
            email = request.session.get('email')
            cursor.close()
    context = {'judul' : judul, 'timestamp' : timestamp, 'email' : email}

    return render(request, 'create_form_pembuatan_donasi.html', context)
@pengguna
def read_donasi(request):
    with connection.cursor() as cursor:
        cursor.execute(
                    "SET SEARCH_PATH TO SIDONA SELECT * FROM DONASI WHERE email=%s ;",
                    [request.session.get('email')])
        data = cursor_fetchall(cursor)
        cursor.close()
    Context = {'isi' : data}
    
    return render(request, 'read_data_donasi_penggalangan_dana.html', Context)

def tambah_wishlist(request):
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PAT TO SIDONA INSERT INTO WISHLIST_DONASI VALUES(%s,%s);",
        [request.session.get('email'), request.GET.get('id_t')])
        cursor.close()
    cek_penggalangan_dana()
@pengguna
def read_detail_donasi(request):
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO SIDONA SELECT * FROM DONASI WHERE email =%s AND idPD = %s LIMIT 1;"
        ,[request.session.get('email'), request.GET.get('id_de')])
        data = cursor.fetchone()
        if data is None:
            return redirect('trigger_empat:profil-pengguna')
        # columns = [col[0] for col in cursor.description]
        # datum = dict(zip(columns,  data)) 
        date_db = data[1]
        formatted_date = date_db.strftime("%Y-%m-%d %H:%M:%S")
        datum = {}
        datum['email'] = data[0]
        datum['timestamp'] = formatted_date
        datum['nominal'] = data[2]
        datum['metodeBayar'] = data[3]
        datum['status'] = data[4]
        datum['doa'] = data[5]
        datum['idPD'] = data[6]
        datum['idStatusPembayaran'] = data[7]
        cursor.close()
    context = {'data' : datum}
        
    return render(request,'read_detail_donasi.html' ,context)