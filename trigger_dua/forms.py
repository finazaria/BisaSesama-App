# from django import forms
# from django.db import connection, transaction, IntegrityError
#
#
# class PilihKategoriForm():
#     def clean(self):
#         id = self.cleaned_data.get("id")
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT id FROM kategori_pd;")
#
# class IsiPasienForm(forms.Form):
#     nik = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=20
#     )
#     nama = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#     tanggal_lahir = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Please use format YYYY-MM-DD'
#         }),
#         max_length=50
#     )
#     alamat_pasien = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control',
#                                      'rows': 3}),
#     )
#     pekerjaan = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#
#
# class CekPasienForm(forms.Form):
#     nik = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=20
#     )
#
#     def cari_nik(self):
#         id = self.cleaned_data.get('nik')
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM PASIEN WHERE nik = %s",
#                            [id])
#             if cursor.fetchone() is None:
#                 raise forms.ValidationError("Pasien tidak ditemukan")
#         return id
#
#
# class PasienForm(IsiPasienForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['nik'].required = True
#
#
# class BuatPasienForm(IsiPasienForm):
#     def save(self):
#         cd = self.cleaned_data
#         with connection.cursor() as cursor:
#             cursor.execute("INSERT INTO PASIEN VALUES(%s, %s, %s, %s, %s)",
#                            [cd.get("nik"), cd.get("nama"),
#                             cd.get("tanggal_lahir"), cd.get("alamat_pasien"),
#                             cd.get("pekerjaan"), ])
#
#
# class IsiRumahIbadahForm(forms.Form):
#     nosertifikat = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=20
#     )
#     nama = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#     alamat_rumah_ibadah = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control',
#                                      'rows': 3}),
#     )
#     jenis = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#
#
# class CekRumahIbadahForm(forms.Form):
#     nosertifikat = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=20
#     )
#
#     def cari_nosertifikat(self):
#         id = self.cleaned_data.get('nosertifikat')
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM RUMAH_IBADAH WHERE nosertifikat = %s",
#                            [id])
#             if cursor.fetchone() is None:
#                 raise forms.ValidationError("Rumah ibadah tidak ditemukan")
#         return id
#
#
# class RumahIbadahForm(IsiRumahIbadahForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['nosertifikat'].required = True
#
#
# class BuatRumahIbadahForm(IsiRumahIbadahForm):
#     def save(self):
#         cd = self.cleaned_data
#         with connection.cursor() as cursor:
#             cursor.execute("INSERT INTO RUMAH_IBADAH VALUES(%s, %s, %s, %s)",
#                            [cd.get("nosertifikat"), cd.get("nama"),
#                             cd.get("alamat_rumah_ibadah"), cd.get("jenis"), ])
#
#
# class IsiPenggalanganDanaForm(forms.Form):
#     id_pd = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     email_penggalang_dana = forms.EmailField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=50,
#         initial="",
#         required=False
#     )
#
#     judul = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control',
#                                      'rows': 3}),
#     )
#
#     deskripsi = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control',
#                                      'rows': 3}),
#     )
#
#     kota = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#
#     provinsi = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#
#     deadline_penggalangan_dana = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Please use format YYYY-MM-DD'
#         }),
#         max_length=50
#     )
#
#     jumlah_target_dana = forms.CharField(
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Tuliskan dalam Rupiah'}),
#         max_length=20
#     )
#
#     kategori = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     nik_pasien = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     nama_pasien = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=50,
#         initial="",
#         required=False
#     )
#
#     penyakit_utama = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#
#     no_sertifikat = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     kategori_aktivitas = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#
#     berkas_penggalangan_dana = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         max_length=50
#     )
#
#
# class NewPenggalanganDanaForm(IsiPenggalanganDanaForm):
#     def save(self):
#         cd = self.cleaned_data
#         with connection.cursor() as cursor:
#             cursor.execute("INSERT INTO APOTEK VALUES(%s, %s, %s, %s, %s, %s, Belum Terverifikasi, %s)",
#                            [cd.get("id"), cd.get("judul"), cd.get("deskripsi"),
#                             cd.get("kota"), cd.get("provinsi"), cd.get("berkas_penggalangan_dana"),
#                             cd.get("deadline_penggalangan_dana"), cd.get("jumlah_target_dana")
#                             ])
#
#
# class BuatRumahIbadahForm(IsiRumahIbadahForm):
#     def save(self):
#         cd = self.cleaned_data
#         with connection.cursor() as cursor:
#             cursor.execute("INSERT INTO RUMAH_IBADAH VALUES(%s, %s, %s, %s)",
#                            [cd.get("nosertifikat"), cd.get("nama"),
#                             cd.get("alamat_rumah_ibadah"), cd.get("jenis"), ])
#
#
# class ReadDetailPDForm(forms.Form):
#     id_pd = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     email_penggalang_dana = forms.EmailField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=50,
#         initial="",
#         required=False
#     )
#
#     judul = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control',
#                                      'rows': 3, 'readonly': True}),
#     )
#
#     deskripsi = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control',
#                                      'rows': 3, 'readonly': True}),
#     )
#
#     kota = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
#         max_length=50
#     )
#
#     provinsi = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
#         max_length=50
#     )
#
#     deadline_penggalangan_dana = forms.CharField(
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Please use format YYYY-MM-DD', 'readonly': True
#         }),
#         max_length=50
#     )
#
#     jumlah_target_dana = forms.CharField(
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Tuliskan dalam Rupiah', 'readonly': True}),
#         max_length=20
#     )
#
#     kategori = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     nik_pasien = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     nama_pasien = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=50,
#         initial="",
#         required=False
#     )
#
#     penyakit_utama = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
#         max_length=50
#     )
#
#     no_sertifikat = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control',
#                                       'readonly': True}),
#         max_length=20,
#         initial="",
#         required=False
#     )
#
#     kategori_aktivitas = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
#         max_length=50
#     )
#
#     berkas_penggalangan_dana = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
#         max_length=50
#     )
#
#     jumlah_terkumpul = forms.CharField(
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Tuliskan dalam Rupiah', 'readonly': True}),
#         max_length=20
#     )
#
#     jumlah_terpakai = forms.CharField(
#         widget=forms.NumberInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Tuliskan dalam Rupiah', 'readonly': True}),
#         max_length=20
#     )
#
#
# class Komorbid(forms.Form):
#     pilihanKomorbid = []
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         with connection.cursor() as cursor:
#             cursor.execute('set search_path to tk_sidona')
#             cursor.execute("SELECT PDD.id, PDD.judul, PDK.penyakit, K.komorbid "
#                            "FROM penggalangan_dana_pd AS PDD, pd_kesehatan as PDK, komorbid AS K "
#                            "WHERE PDD.id = PDK.idpd AND K.idpd = PDK.idpd ORDER BY PDD.id;")
#             self.fields['id'].choices = cursor.fetchall()
#
#     id = forms.ChoiceField(choices=pilihanKomorbid, widget=forms.Select(attrs={'class': 'form-control'}))
#     penyakit = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     komorbid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#
# class UpdateKomorbid(Komorbid):
#     oldId = forms.CharField(
#         widget=forms.HiddenInput(attrs={'class': 'form-control', 'readonly': True}),
#         max_length=20,
#     )
#
#     def clean(self):
#         oldId = self.cleaned_data.get("oldId")
#         id = self.cleaned_data.get("id")
#         with connection.cursor() as cursor:
#             cursor.execute('set search_path to tk_sidona')
#             cursor.execute("SELECT PDD.id, PDD.judul, PDK.penyakit, K.komorbid "
#                            "FROM penggalangan_dana_pd AS PDD, pd_kesehatan as PDK, komorbid AS K "
#                            "WHERE PDD.id = PDK.idpd AND K.idpd = PDK.idpd AND PDK.idpd != % s;", [oldId])
#
#     def save(self):
#         cd = self.cleaned_data
#         try:
#             with connection.cursor() as cursor:
#                 with transaction.atomic():
#                     cursor.execute("""\
#                     UPDATE komorbid SET penyakit = %s WHERE idpd = %s""",
#                                    [cd.get("penyakit"), cd.get("oldId")])
#         except IntegrityError:
#             pass
#
#
# class CreateKomorbid(Komorbid):
#     def clean(self):
#         id = self.cleaned_data.get("id")
#         with connection.cursor() as cursor:
#             cursor.execute('set search_path to tk_sidona')
#             cursor.execute("SELECT PDD.id, PDD.judul, PDK.penyakit, K.komorbid "
#                            "FROM penggalangan_dana_pd AS PDD, pd_kesehatan as PDK, komorbid AS K "
#                            "WHERE PDD.id = PDK.idpd AND K.idpd = PDK.idpd;")
#
#     def save(self):
#         cd = self.cleaned_data
#         with connection.cursor() as cursor:
#             cursor.execute('set search_path to tk_sidona')
#             cursor.execute("INSERT INTO KOMORBID VALUES(%s, %s)",
#                            [cd.get("id"), cd.get("komorbid")])
