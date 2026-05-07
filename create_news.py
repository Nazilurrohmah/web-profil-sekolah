import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_project.settings')
django.setup()

from main.models import Berita

content = """📣 PENGUMUMAN PENERIMAAN MURID BARU (PPDB) 2026-2027 📣

Telah Dibuka Pendaftaran Peserta Didik Baru (PPDB) Tahun Ajaran 2026-2027!
Ayo segera daftarkan putra-putri Anda. PENDAFTARAN GRATIS!

SYARAT PENDAFTARAN:
- Foto Copy Akta Kelahiran 1 Lembar
- Foto Copy KK 1 Lembar
- Pas Foto 3x4 Sebanyak 3 Lembar
- Mengisi Formulir Pendaftaran
- Foto Copy Kartu PIP atau SKTM
- Foto Copy KTP Ortu Sebanyak 2 Lembar
- Foto Copy Ijazah MI/SD/MTs/SMP 3 Lembar
- Niat Kuat Dalam KBM dan Pesantren

ALUR & JADWAL PENDAFTARAN:
- Tanggal: 1 Januari s.d 30 Juni 2026
- Waktu: 08.00 s.d 20.00 WIB
- Tempat: Sekretariat SMP/MA/PP. Nurul Islam

Kami memiliki program unggulan seperti Amtsilati, Kaligrafi, Hadrah, dll. Asrama juga 
tersedia untuk putra dan putri.

Untuk informasi lebih lanjut, gunakan Chatbot PPDB di pojok kanan layar, atau hubungi 
CP kami yang tertera di bagian bawah website. Siapkan berkas Anda dan mari bergabung 
bersama SMP Nurul Islam!"""

# Check if it already exists to avoid duplicates if run multiple times
if not Berita.objects.filter(title__icontains='PPDB').exists():
    Berita.objects.create(
        title='Pengumuman Penerimaan Murid Baru (PPDB) 2026-2027',
        content=content.strip()
    )
    print("Berita created successfully.")
else:
    print("Berita already exists.")
