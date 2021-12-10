from django.shortcuts import redirect, render
from django.db import connection
from pengguna.views import pengguna, cursor_fetchall
from trigger_lima.forms import *

# Create your views here.

@pengguna
def form_pencairan_dana(request):
    with connection.cursor() as cursor :
        cursor.execute("SET SEARCH PATH TO TK_SIDONA")
        cursor.execute("SELECT * FROM PENGGALANG_DANA P WHERE P.id = %s", [request.session("id")])
        data = cursor_fetchall(cursor)
    context = {'data' : data}
    return render(request, 'create_form_pencairan_dana.html', context)

def data_penggalang_dana(request):
    return render(request, 'profil')