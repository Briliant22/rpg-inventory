# Role-Playing-Games Inventory System

Muhammad Najmi Briliant (2206082820)
PBP C

## Tautan Aplikasi

[Link to Role-Playing-Games Inventory System](https://najmibriliant-rpginventory.adaptable.app)

## Tugas 2: Implementasi MVT Model pada Django

> 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat sebuah proyek Django baru.

- Sebelum meng-inisialisasi aplikasi, developer pertama membuat direktori lokal bernama `rpg_inventory` dan repositori GitHub terlebih dahulu. Direktori lokal tersebut dihubungkan dengan repositori menggunakan perintah `git branch -M main` untuk membuat main branch dan perintah `git remote add origin <URL_REPO>` untuk menghubungkan direktori lokal dengan repositori GitHub.
- Setelah kedua repositori terhubung, developer membuat virtual environment pada direktori lokal dengan menggunakan perintah `python -m venv env`. Setelah virtual environment dibuat, dapat diaktifkan dengan perintah `source env/bin/activate`. Pada direktori utama, perlu ditambahkan file `requirements.txt` yang menjadi daftar dependensi dari proyek ini. Dependensi tersebut harus di-install pada direktori proyek dengan perintah `pip install -r requirements.txt`. Terakhir, proyek dapat dibuat dengan menjalankan perintah `django-admin startproject rpg_inventory .`.

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

- Setelah proyek selesai dibuat, developer dapat membuat direktori main di dalam direktori utama dengan menjalankan perintah `python manage.py startapp main`. Folder tersebut berfungsi sebagai struktur inti dari proyek ini. Developer juga mendaftarkan folder main ke dalam proyek dengan menambahkan `main` dalam variabel `INSTALLED_APPS` dalam file `settings.py`.

- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.

- Developer menambahkan path ke dalam variabel `urlpatterns` pada `urls.py` agar rute URL aplikasi `main` terdefinisi. Path terdiri dari route, function pada `views.py` , dan parameter name. Lalu, developer mengkonfigurasi routing URL proyek

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
>     Terdapat beberapa alasan mengapa developer menggunakan virtual environment untuk mendevelop aplikasi web berbasis Django, yaitu:

- Virtual environment digunakan untuk mengelola dan meng-encapsulate dependensi proyek agar terisolasi dan tidak mempengaruhi proyek lainnya yang mungkin menggunakan versi Django berbeda. Virtual environment juga memungkinkan developer untuk meng-install dan mengelola dependensi proyek secara terpisah dari dependensi proyek lain.

- Virtual environment memberikan kemudahan bagi developer dalam mengelola dan mengganti versi paket. Developer dapat mengaktifkan atau menonaktifkan virtual environment sesuai kebutuhan proyek, dan dapat menghapusnya jika proyek sudah selesai.

Penggunaan virtual environment sangat direkomendasikan dalam pengembangan Django, sebenarnya pembuatan aplikasi web berbasis Django tanpa menggunakan virtual environment bisa dilakukan. Namun, ini bisa menjadi praktik yang tidak dianjurkan karena mengelola dependensi dan isolasi proyek akan menjadi lebih rumit dan kurang terstruktur. Virtual environment membantu menjaga kebersihan dan kerapihan dalam pengembangan web dengan Django dan membuatnya lebih mudah untuk mengelola proyek-proyek yang berbeda dalam lingkungan Python yang bersih dan terisolasi.

> 4.  Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
>     MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola arsitektur perangkat lunak yang berbeda yang digunakan dalam pengembangan aplikasi. Mereka memiliki beberapa persamaan konseptual, tetapi ada perbedaan signifikan dalam cara mereka mengorganisasi kode dan aliran data dalam aplikasi.

Konsep dasarnya tetap menggunakan komponen berikut:

- Model: Representasi dari data dan logika bisnis dalam aplikasi. Model mengelola data, mengelola pembaruan, dan memberi tahu View tentang perubahan data.

- View: Bertanggung jawab untuk menampilkan data kepada pengguna dan mengirim masukan pengguna ke Controller. View tidak memiliki pengetahuan tentang data atau logika bisnis, hanya tampilan yang digambarkan.

Tetapi terdapat perbedaan dalam pengelolaan input dan tampilan, yaitu pada komponen:

- Controller: Menerima masukan dari pengguna dan mengkoordinasikan dengan Model dan View. Controller mengelola aliran logika bisnis dan memutuskan tampilan mana yang harus diperbarui.

- Template: Merupakan tampilan dalam Django, yang digunakan untuk merender data dari Model menjadi HTML yang akan ditampilkan kepada pengguna. Template berisi kode HTML dengan penambahan sintaksis Django untuk menyisipkan data dinamis.

- ViewModel: Bertindak sebagai perantara antara Model dan View. Ini adalah komponen yang mengambil data dari Model dan memformatnya agar dapat ditampilkan dengan mudah oleh View. ViewModel juga merespons perintah dari View dan mengubah Model sesuai kebutuhan.

Singkatnya, MVC, MVT, dan MVVM adalah tiga pola arsitektur yang berbeda dengan konsep dasar yang serupa dalam memisahkan tampilan, logika bisnis, dan data. Perbedaan utama terletak dalam cara mereka mengorganisasi komponen-komponen ini dan berinteraksi di dalam aplikasi. Pemilihan pola yang tepat tergantung pada kebutuhan proyek dan kerangka kerja yang digunakan.
