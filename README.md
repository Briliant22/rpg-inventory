# Role-Playing-Games Inventory System

Muhammad Najmi Briliant (2206082820)
PBP C

## Tautan Aplikasi

[Link to Role-Playing-Games Inventory System](https://najmibriliant-rpginventory.adaptable.app)

## Tugas 2: Implementasi MVT Model pada Django

> 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat sebuah proyek Django baru.
      Sebelum meng-inisialisasi aplikasi, developer pertama membuat direktori lokal bernama `rpg_inventory` dan repositori GitHub terlebih dahulu. Direktori lokal tersebut dihubungkan dengan repositori menggunakan perintah `git branch -M main` untuk membuat main branch dan perintah `git remote add origin <URL_REPO>` untuk menghubungkan direktori lokal dengan repositori GitHub.

      Setelah kedua repositori terhubung, developer membuat virtual environment pada direktori lokal dengan menggunakan perintah `python -m venv env`. Setelah virtual environment dibuat, dapat diaktifkan dengan perintah `source env/bin/activate`. Pada direktori utama, perlu ditambahkan file `requirements.txt` yang menjadi daftar dependensi dari proyek ini. Dependensi tersebut harus di-install pada direktori proyek dengan perintah `pip install -r requirements.txt`. Terakhir, proyek dapat dibuat dengan menjalankan perintah `django-admin startproject rpg_inventory .`.

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.
      Setelah proyek selesai dibuat, developer dapat membuat direktori main di dalam direktori utama dengan menjalankan perintah `python manage.py startapp main`. Folder tersebut berfungsi sebagai struktur inti dari proyek ini. Developer juga mendaftarkan folder main ke dalam proyek dengan menambahkan `main` dalam variabel `INSTALLED_APPS` dalam file `settings.py`.

- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.
      Developer menambahkan path ke dalam variabel `urlpatterns` pada `urls.py` agar rute URL aplikasi `main` terdefinisi. Path terdiri dari route, function pada `views.py` , dan parameter name. Lalu, developer mengkonfigurasi routing URL proyek

- [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
  - `name` sebagai nama _item_ dengan tipe `CharField`.
  - `amount` sebagai jumlah _item_ dengan tipe `IntegerField`.
  - `description` sebagai deskripsi _item_ dengan tipe `TextField`.

a

- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

a

- [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

a

- [x] Melakukan _deployment_ ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

a

> 2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![MVT Model Chart](mvt_model.jpg)

> 3.  Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

a

> 4.  Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
