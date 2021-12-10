from django import forms
from django.db import connection
from pengguna.views import cursor_fetchall

class pencairan_dana(forms.Form) :
    saldo_donapay = forms.DecimalField(required =False, disabled=True,
        widget= forms.EmailInput(
            attrs ={
                "class" : "form-control",
                "aria-label" : "disable input example"
            }
        )
    )
    penggalangan_dana = forms.CharField(required=False, disabled=True,
        widget = forms.TextInput(attrs = {
                "class" : "form-control",
                "name"  : "judul_penggalangan_dana",
                "aria-label" : "disable input example"
            }
        )
    )
    nominal = forms.DecimalField(required=True,
        widget = forms.TextInput(attrs = {
                "class" : "form-control",
                "name"  : "nominal",
                "aria-label" : "disable input example"
            }
        )
    )
    keterangan = forms.CharField(required=True,
        widget=forms.NumberInput(
            attrs = {
                "class" : "form-control",
                "name" : "keterangan",
                "aria-label" : "default input example"
            }
        )
    )

    def save(self):
        saldo_donapay = self.cleaned_data['saldo_donapay']
        penggalangan_dana = self.cleaned_data['penggalangan_dana']
        nominal = self.cleaned_data['nominal']
        keterangan = self.cleaned_data['keterangan']

        with connection.cursor() as cursor :
            cursor.execute("SET SEARCH PATH TO TK_SIDONA")
            cursor.execute("SELECT id FROM PENGGALANG_DANA WHERE ")