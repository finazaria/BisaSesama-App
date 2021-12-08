from django import forms
from django.db import connection
from passlib.hash import pbkdf2_sha256
from random import choice

# LOGIN HANDLING
class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'example@email.com'}),
        max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        max_length=128)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')


class AdminLogin(LoginForm) :
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM ADMIN WHERE email=%s LIMIT 1;",
                [email])
            data = cursor.fetchone()
        if data is None:
            self.add_error('email', 'Email tidak terdaftar')
        elif not pbkdf2_sha256.verify(password, data[2]):
            self.add_error('password', 'Password salah')

class PenggalangDanaLogin(LoginForm) :
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM PENGGALANG_DANA WHERE email=%s LIMIT 1;",
                [email])
            data = cursor.fetchone()
        if data is None:
            self.add_error('email', 'Email tidak terdaftar')
        elif not pbkdf2_sha256.verify(password, data[2]):
            self.add_error('password', 'Password salah')


# REGISTER HANDLING
class PilihRoleForm(forms.Form):
    ROLE_CHOICE = [('PENGGALANG_DANA', 'Penggalang Dana'),
                   ('ADMIN', 'Admin')]
    peran = forms.ChoiceField(choices=ROLE_CHOICE,
                              widget=forms.Select(attrs={'class': 'form-control'}))

class AdminForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'}),
        max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        max_length=128)
    nama_lengkap = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    nomor_hp = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0xx (w/o country code)'}),
        max_length=20
    )

    def clean_email(self):
        data = self.cleaned_data.get('email')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM ADMIN WHERE email=%s LIMIT 1",
                           [data])
            row = cursor.fetchone()
        if row is not None:
            raise forms.ValidationError("Email sudah terdaftar")
        return data

    def clean_password(self):
        data = self.cleaned_data.get('password')
        data = pbkdf2_sha256.hash(data, rounds=200000, salt_size=16)
        return data

    def save(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        nama_lengkap = self.cleaned_data.get('nama_lengkap')
        nomor_hp = self.cleaned_data.get('nomor_hp')

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO ADMIN VALUES(%s,%s,%s,%s)",
                           [email, nomor_hp, password, nama_lengkap])


class PenggalangDanaForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control'}),
        max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        max_length=128)
    nama_lengkap = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    nomor_hp = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0xx (w/o country code)'}),
        max_length=20
    )
    alamat = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=200
    )
    nama_bank = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    nomor_rekening = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    ROLE_CHOICE = [('INDIVIDU', 'Individu'),
                   ('ORGANISASI', 'Organisasi')]
    peran = forms.ChoiceField(choices=ROLE_CHOICE,
                              widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_email(self):
        data = self.cleaned_data.get('email')
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM PENGGALANG_DANA WHERE email=%s LIMIT 1",
                           [data])
            row = cursor.fetchone()
        if row is not None:
            raise forms.ValidationError("Email sudah terdaftar")
        return data

    def clean_password(self):
        data = self.cleaned_data.get('password')
        data = pbkdf2_sha256.hash(data, rounds=200000, salt_size=16)
        return data

    def save(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        nama_lengkap = self.cleaned_data.get('nama_lengkap')
        nomor_hp = self.cleaned_data.get('nomor_hp')
        alamat = self.cleaned_data.get('alamat')
        nama_bank = self.cleaned_data.get('nama_bank')
        nomor_rekening = self.cleaned_data.get('nomor_rekening')

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO PENGGALANG_DANA VALUES(%s,%s,%s,%s,%s,%s,%s)",
                           [email, password, nama_lengkap, nomor_hp, alamat, nama_bank, nomor_rekening])

class IndividuForm(PenggalangDanaForm):
    nik = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    tanggal_lahir = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Format: mm/dd/yyyy'}),
    )
    GENDER_CHOICES = [
        ('L', 'Laki-Laki'),
        ('P', 'Perempuan'),
        ('U', 'Tidak Ingin Memberitahu')
    ]
    jenis_kelamin = forms.CharField(
        widget=forms.Select(
            choices=GENDER_CHOICES,
            attrs={'class': 'form-control'},),
        max_length=1,
    )
    # FOTO KTP
    # Insert Code Here

    def save(self):
        super().save()
        email = self.cleaned_data.get('email')
        nik = self.cleaned_data.get('nik')
        tanggal_lahir = self.cleaned_data.get('tanggal_lahir')
        jenis_kelamin = self.cleaned_data.get('jenis_kelamin')

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO PENGGALANG_DANA VALUES(%s,%s,%s,%s)",
                           [email, nik, tanggal_lahir, jenis_kelamin])


class OrganisasiForm(PenggalangDanaForm):
    nama_organisasi = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    nomor_akta_pendirian = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        max_length=50
    )
    no_telp_organisasi = forms.CharField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': '0xx (w/o country code)'}),
        max_length=20
    )
    tahun_berdiri = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        max_length=4
    )
    # FOTO AKTA PENDIRIAN
    # INSERT CODE HERE

    def save(self):
        super().save()
        email = self.cleaned_data.get('email')
        nap = self.cleaned_data.get('nap')
        nama_organisasi = self.cleaned_data.get('nama_organisasi')
        no_telp_organisasi = self.cleaned_data.get('no_telp_organisasi')
        tahun_berdiri = self.cleaned_data.get('tahun_berdiri')

        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO PENGGALANG_DANA VALUES(%s,%s,%s,%s,%s)",
                           [email, nap, nama_organisasi, no_telp_organisasi, tahun_berdiri])