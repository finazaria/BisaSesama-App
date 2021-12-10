from django import forms


from django.db import connection
from django.forms.fields import EmailField
from django.forms.widgets import Select
from pengguna.views import cursor_fetchall
class Tambah_Donasi(forms.Form):
    metode_bayar = [('Transfer' , 'Transfer'), ('DonaPay' ,'DonaPay')]
    theStatus = [('Anonim','Ya'), ('Non-anonim','Tidak')]  


    email = forms.EmailField(required =False, disabled=True,
        widget= forms.EmailInput(
            attrs ={
                "class" : "form-control",
                "aria-label" : "disable input example"
            }
        )
    )
    timeStamp = forms.CharField(required=False, disabled=True,
        widget = forms.TextInput(attrs = {
                "class" : "form-control",
                "name"  : "TimeStamp",
                "aria-label" : "disable input example"
            }
        )
    )
    judul = forms.CharField(required=False, disabled=True,
        widget = forms.TextInput(attrs = {
                "class" : "form-control",
                "name"  : "judul",
                "aria-label" : "disable input example"
            }
        )
    )
    Nominal = forms.DecimalField(required=True,
        widget=forms.NumberInput(
            attrs = {
                "class" : "form-control",
                "name" : "nominal",
                "aria-label" : "default input example"
            }
        )

    )
    metodeBayar = forms.ChoiceField(required=True, choices=metode_bayar,
        widget= forms.Select(
            attrs={
                "id" : "metodeBayar",
                "class" : "form-control mb-4",
                "name" : "metodeBayar",
                "aria-label" : "Default select example"
            }
        )
    )
    Status = forms.ChoiceField(required=True, choices=theStatus,
        widget= forms.Select(
            attrs={
                "id" : "Anonim",
                "class" : "form-control mb-4",
                "name" : "status",
                "aria-label" : "Default select example"
            }
        )
    )
    doa = forms.CharField(required=True,
        widget = forms.Textarea(
            attrs= {
                "class" : "form-control",
                "name" : "message",
                "rows" : "5"
            }
        )
    )

    def save(self):
        email_d = self.cleaned_data['email']
        timestamp_d = self.cleaned_data['timeStamp']
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