from django.shortcuts import render, redirect
from django.db import connection, transaction, IntegrityError
from .forms import *
from django.contrib import messages

def user_login_required(function):
    def wrapper(request, *args, **kwargs):
        email = request.session.get('email')
        if email is None:
            return redirect('/login/')
        else:
            return function(request, *args, **kwargs)
    return wrapper

def cursor_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

@user_login_required
def create_penggalangan_dana(request):
    if request.session.get("role") != "PENGGALANG_DANA":
        return redirect('/trigger_dua/penggalangan_dana/')
    if request.method == 'POST':
        form = PilihKategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/trigger_dua/penggalangan_dana/")
    if request.method == 'GET':
        form = PilihKategoriForm()
    context = {'form': form}
    return render(request, 'create_kategori_penggalangan_dana.html', context)

@user_login_required
def form_kategori(request):
    return render(request, 'create_kategori_penggalangan_dana.html')

@user_login_required
def form_pasien(request):
    return render(request, 'create_form_pasien.html')

@user_login_required
def cek_pasien(request):
    return render(request, 'cek_pasien_terdaftar.html')

@user_login_required
def form_rumah_ibadah(request):
    return render(request, 'create_form_rumah_ibadah.html')

@user_login_required
def cek_rumah_ibadah(request):
    return render(request, 'cek_rumah_ibadah_terdaftar.html')

@user_login_required
def form_penggalangan_dana(request):
    return render(request, 'create_form_penggalangan_dana.html')

@user_login_required
def read_penggunaan_dana(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT timestamp, nominal, deskripsi "
                       "FROM RIWAYAT_PENGGUNAAN_DANA "
                       "WHERE idpd = % s, timestamp = % s;", request.GET.get('id_pd'), request.get('timestamp'))
        data_pdd = cursor_fetchall(cursor)

        context = {'data': data_pdd}
    return render(request, 'read_penggalangan_dana_pribadi.html', context)

@user_login_required
def read_pdd_pribadi(request):
    penggalangan_dana = 0
    penggalangan_dana_aktif = 0
    with connection.cursor() as cursor:
        cursor.execute('set search_path to public')
        email = request.session["email"]
        cursor.execute('set search_path to tk_sidona')
        print(email)
        cursor.execute("SELECT PDD.id, PDD.judul, PDD.kota, PDD.provinsi, PDD.tanggal_aktif_awal, PDD.tanggal_aktif_akhir, PDD.sisa_hari, "
                       "PDD.jumlah_dibutuhkan, KPD.nama_kategori, PDD.status_verifikasi "
                       "FROM penggalangan_dana_pd AS PDD, kategori_pd AS KPD "
                       "WHERE PDD.id_kategori = KPD.id AND PDD.email_user = %s "
                       "ORDER BY PDD.id;", [email])
        data_pdd = cursor_fetchall(cursor)
        print(data_pdd)

        penggalangan_dana = len(data_pdd)

        for i in range(len(data_pdd)):
            if data_pdd[i]["status_verifikasi"] == "Terverifikasi":
                penggalangan_dana_aktif += 1

    context = {'data': data_pdd, 'pdd': penggalangan_dana, 'aktif': penggalangan_dana_aktif}
    return render(request, 'read_penggalangan_dana_pribadi.html', context)

@user_login_required
def read_donatur(request):
    with connection.cursor() as cursor:

        cursor.execute("SELECT email, timestamp, nominal, doa"
                       "FROM DONASI"
                       "WHERE idpd = %s, timestamp = %s;", request.GET.get('id_pd'), request.get('timestamp'))
        data_pdd = cursor_fetchall(cursor)

    context = {'data': data_pdd}
    return render(request, 'read_penggalangan_dana_pribadi.html', context)

@user_login_required
def read_pdd(request):

    return render(request, 'read_penggalangan_dana.html')

@user_login_required
def delete_penggalangan_dana(request):
    if request.session.get("role") != "PENGGALANG_DANA":
        return redirect('/trigger_dua/penggalangan_dana/')
    if request.method == 'GET':
        if request.GET.get('id') is None:
            return redirect('/trigger_dua/penggalangan_dana/')
        else:
            id = request.GET.get('id')
            try:
                with connection.cursor() as cursor:
                    with transaction.atomic():
                        cursor.execute("""\
                        DELETE FROM penggalangan_dana_pd WHERE id=%s\
                        """, [id])
            except IntegrityError:
                pass
            return redirect('/trigger_dua/penggalangan_dana/')

@user_login_required
def cairkan_pdd(request):
    return render(request, 'read_penggalangan_dana_pribadi.html')

@user_login_required
def read_komorbid(request):
    with connection.cursor() as cursor:
        cursor.execute('set search_path to public')
        email = request.session["email"]

        cursor.execute('set search_path to tk_sidona')

        cursor.execute("SELECT PDD.id, PDD.judul, PDK.penyakit, K.komorbid "
                       "FROM penggalangan_dana_pd AS PDD, pd_kesehatan as PDK, komorbid AS K "
                       "WHERE PDD.id = PDK.idpd AND K.idpd = PDK.idpd AND PDD.email_user = %s "
                       "ORDER BY PDD.id;", [email])
        dataKomorbid = cursor_fetchall(cursor)
        print(dataKomorbid)

    context = {'data': dataKomorbid}


    return render(request, 'read_komorbid.html', context)

@user_login_required
def create_komorbid(request):
    context = {}
    context['pdk'] = []
    with connection.cursor() as cursor:
        cursor.execute('set search_path to public')
        email = request.session["email"]
        cursor.execute("set search_path to tk_sidona")
        cursor.execute("SELECT * from PD_KESEHATAN AS PDK, PENGGALANGAN_DANA_PD AS PDD "
                       "WHERE PDK.idpd = PDD.id AND PDD.email_user = %s ", [email])
        pdk = cursor.fetchall()

        for i in range(len(pdk)):
            context["pdk"].append([
                pdk[i][0]
            ])
        cursor.execute("set search_path to public")
    if request.session.get("role") != "PENGGALANG_DANA":
        return redirect('/trigger_dua/komorbid/')
    if request.method == 'POST':
        # form = Komorbid(request.POST)
        # if form.is_valid():
        #     form.save()
        #     cd = form.cleaned_data
        with connection.cursor() as cursor:
            id = request.POST["pdk"]
            komorbid = request.POST["komorbid"]
            cursor.execute('set search_path to tk_sidona')
            try:
                cursor.execute("INSERT INTO KOMORBID VALUES(%s, %s)",
                           [id, komorbid])
                return redirect("/trigger_dua/komorbid/")
            except:
                messages.add_message(request, messages.WARNING,
                                     f"Maaf, pasangan ID Penggalangan Dana dan Penyakit Komorbid sudah ada!")
    # elif request.method == 'GET':
    #     form = CreateKomorbid()
    # context["form"] = form

    return render(request, 'create_komorbid.html', context)

@user_login_required
def update_komorbid(request, id, penyakit):
    context = {}
    context["id"] = id
    context["penyakit"] = penyakit
    if request.session.get("role") != "PENGGALANG_DANA":
        return redirect('/trigger_dua/komorbid/')
    if request.method == 'POST':
        with connection.cursor() as cursor:
            cursor.execute("set search_path to tk_sidona")
            cursor.execute("update pd_kesehatan set penyakit = %s where idpd = %s", [request.POST["penyakit"], id])
            cursor.execute("set search_path to public")
        return redirect('/trigger_dua/komorbid/')
    return render(request, 'update_komorbid.html', context)

@user_login_required
def delete_komorbid(request, id, komorbid):
    if request.session.get("role") != "PENGGALANG_DANA":
        return redirect('/trigger_dua/komorbid/')
    if request.method == 'GET':
        try:
            with connection.cursor() as cursor:
                cursor.execute("set search_path to tk_sidona")
                cursor.execute("""\
                DELETE FROM KOMORBID WHERE idpd=%s AND komorbid=%s
                """, [id, komorbid])
        except IntegrityError:
            pass

    return redirect('/trigger_dua/komorbid/')