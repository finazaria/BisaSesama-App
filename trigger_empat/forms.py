from django import forms


from django.db import connection
from pengguna.views import cursor_fetchall
class Tambah_Donasi(forms.Form):
    email = forms.EmailField()
    timeStamp = forms.CharField()
    judul = forms.CharField()
    Nominal = forms.IntegerField()
    metodeBayar = forms.CharField()
    Status = forms.CharField()
    doa = forms.CharField()

    def save(self):
        email_d = self.cleaned_data['email']
        timestamp_d = self.cleaned_data['timestamp']
        judul_d = self.cleaned_data['judul']
        nominal_d = self.cleaned_data['Nominal']
        metodebayar_d = self.cleaned_data['metodeBayar']
        status_d = self.cleaned_data['Status']
        doa_d = self.cleaned_data['doa']

        with connection.cursor() as cursor:
            cursor.execute(
                        "SET SEARCH_PATH TO TK_SIDONA SELECT id FROM PENGGALANG_DANA_PD WHERE judul = %s LIMIT 1;",[judul_d]) 
            data = cursor_fetchall(cursor)
            cursor.close()

        with connection.cursor() as cursor:
            cursor.execute("SET SEARCH_PATH TO SIDONA INSERT INTO DONASI VALUES(%s,%s,%d,%s,%s,%s,%s);"
            ,[email_d,timestamp_d,nominal_d,metodebayar_d,status_d,doa_d,data])

            cursor.close()