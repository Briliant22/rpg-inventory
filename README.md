# Role-Playing-Games Inventory System

Muhammad Najmi Briliant (2206082820)
PBP C

## Tautan Aplikasi

[Link to Role-Playing-Games Inventory System](https://najmibriliant-rpginventory.adaptable.app)

## Tugas 2: Implementasi MVT Model pada Django

> 1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat sebuah proyek Django baru.

Sebelum meng-inisialisasi aplikasi, developer pertama membuat direktori lokal bernama `rpg_inventory` dan repositori GitHub terlebih dahulu. Direktori lokal tersebut dihubungkan dengan repositori menggunakan perintah `git branch -M main` untuk membuat main branch dan perintah `git remote add origin <URL_REPO>` untuk menghubungkan direktori lokal dengan repositori GitHub.
Setelah kedua repositori terhubung, developer membuat virtual environment pada direktori lokal dengan menggunakan perintah `python -m venv env`. Setelah virtual environment dibuat, dapat diaktifkan dengan perintah `env\Scripts\activate.bat`. Pada direktori utama, perlu ditambahkan file `requirements.txt` yang menjadi daftar dependensi dari proyek ini. Dependensi tersebut harus di-install pada direktori proyek dengan perintah `pip install -r requirements.txt`. Terakhir, proyek dapat dibuat dengan menjalankan perintah `django-admin startproject rpg_inventory .`.

- [x] Membuat aplikasi dengan nama `main` pada proyek tersebut.

Setelah proyek selesai dibuat, developer dapat membuat direktori main di dalam direktori utama dengan menjalankan perintah `python manage.py startapp main`. Folder tersebut berfungsi sebagai struktur inti dari proyek ini. Developer juga mendaftarkan folder main ke dalam proyek dengan menambahkan `main` dalam variabel `INSTALLED_APPS` dalam file `settings.py`.

- [x] Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.

Developer menambahkan path ke dalam variabel `urlpatterns` pada `urls.py` agar rute URL aplikasi `main` terdefinisi. Path terdiri dari route, function pada `views.py` , dan parameter name. Lalu, developer mengkonfigurasi routing URL proyek dengan menambahkan path yang terdiri dari route dan fungsi include ke dalam variabel `urlpatterns`. Fungsi include berfungsi untuk mengimpor rute URL aplikasi `main` ke dalam file urls.py proyek.

- [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.

- `name` sebagai nama _item_ dengan tipe `CharField`.
- `amount` sebagai jumlah _item_ dengan tipe `IntegerField`.
- `description` sebagai deskripsi _item_ dengan tipe `TextField`.

Selain atribut wajib, developer juga telah menambahkan beberapa atribut tambahan seperti:

- `price` sebagai harga _item_ dengan tipe `IntegerField`.
- `power` sebagai kekuatan yang dimiliki _item_ dengan tipe `IntegerField`.
- `category` sebagai jenis _item_ dengan tipe `CharField`.

- [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah _template_ HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Developer meng-import function `render` agar bisa melakukan rendering terhadap tampilan `main.html`. Lalu dilanjutkan dengan mendeklarasikan function `show_main` dengan parameter request. Setelah itu, developer menambahkan data `name` dan `category` dalam fungsi `show_main`. Function di atas me-return `render(request, "main.html", context)` untuk menampilkan html pada web server.

- [x] Membuat sebuah _routing_ pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

Di tahap ini, developer meng-import `path` dari `django.urls` dan fungsi `show_app_name` dari file `views.py`. Lalu, developer mengubah variabel `app_name` menjadi `main`. Setelah itu developer menambahkan path yang berisi route, fungsi `show_main`, dan parameter name pada variabel `urlpatterns`.

- [x] Melakukan _deployment_ ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Setelah kerangka dasar aplikasi selesai dibuat, developer melakukan push semua perubahan yang telah dilakukan ke dalam repositori di `rpg_inventory` di GitHub. Menggunakan fitur source control pada GitHub, komentar, commit dan push dapat dengan mudah dilakukan. Setelah perubahan di push ke GitHub, developer dapat mendeploy aplikasi menggunakan Adaptable.io. Dalam hoster tersebut, developer menghubungkan repositori `rpg_inventory` dengan applikasi, memilih `Python App Template` dan `PostgreSQL` sebagai database. Developer juga menyesuaikan versi python menjadi 3.10, dan menerapkan perintah `python manage.py migrate && gunicorn najmibriliant-rpginventory.wsgi` di bagian start command. Terakhir, developer mencentang opsi `HTTP Listener on PORT` dan mendeploy aplikasi

> 2.  Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![MVT Model Chart](mvt_model.jpg)

> 3.  Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Terdapat beberapa alasan mengapa developer menggunakan virtual environment untuk mendevelop aplikasi web berbasis Django, yaitu:

- Virtual environment digunakan untuk mengelola dan meng-encapsulate dependensi proyek agar terisolasi dan tidak mempengaruhi proyek lainnya yang mungkin menggunakan versi Django berbeda. Virtual environment juga memungkinkan developer untuk meng-install dan mengelola dependensi proyek secara terpisah dari dependensi proyek lain.

- Virtual environment memberikan kemudahan bagi developer dalam mengelola dan mengganti versi paket. Developer dapat mengaktifkan atau menonaktifkan virtual environment sesuai kebutuhan proyek, dan dapat menghapusnya jika proyek sudah selesai.

Penggunaan virtual environment sangat direkomendasikan dalam pengembangan Django, sebenarnya pembuatan aplikasi web berbasis Django tanpa menggunakan virtual environment bisa dilakukan. Namun, ini bisa menjadi praktik yang tidak dianjurkan karena mengelola dependensi dan isolasi proyek akan menjadi lebih rumit dan kurang terstruktur. Virtual environment membantu menjaga kebersihan dan kerapihan dalam pengembangan web dengan Django dan membuatnya lebih mudah untuk mengelola proyek-proyek yang berbeda dalam lingkungan Python yang bersih dan terisolasi.

> 4.  Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
MVC (Model-View-Controller), MVT (Model-View-Template), dan MVVM (Model-View-ViewModel) adalah tiga pola arsitektur perangkat lunak yang berbeda yang digunakan dalam pengembangan aplikasi. Mereka memiliki beberapa persamaan konseptual, tetapi ada perbedaan signifikan dalam cara mereka mengorganisasi kode dan aliran data dalam aplikasi.

Konsep dasarnya tetap menggunakan komponen berikut:

- Model: Representasi dari data dan logika bisnis dalam aplikasi. Model mengelola data, mengelola pembaruan, dan memberi tahu View tentang perubahan data.

- View: Bertanggung jawab untuk menampilkan data kepada pengguna dan mengirim masukan pengguna ke Controller. View tidak memiliki pengetahuan tentang data atau logika bisnis, hanya tampilan yang digambarkan.

Tetapi terdapat perbedaan dalam pengelolaan input dan tampilan, yaitu pada komponen:

- Controller: Menerima masukan dari pengguna dan mengkoordinasikan dengan Model dan View. Controller mengelola aliran logika bisnis dan memutuskan tampilan mana yang harus diperbarui.

- Template: Merupakan tampilan dalam Django, yang digunakan untuk merender data dari Model menjadi HTML yang akan ditampilkan kepada pengguna. Template berisi kode HTML dengan penambahan sintaksis Django untuk menyisipkan data dinamis.

- ViewModel: Bertindak sebagai perantara antara Model dan View. Ini adalah komponen yang mengambil data dari Model dan memformatnya agar dapat ditampilkan dengan mudah oleh View. ViewModel juga merespons perintah dari View dan mengubah Model sesuai kebutuhan.

Singkatnya, MVC, MVT, dan MVVM adalah tiga pola arsitektur yang berbeda dengan konsep dasar yang serupa dalam memisahkan tampilan, logika bisnis, dan data. Perbedaan utama terletak dalam cara mereka mengorganisasi komponen-komponen ini dan berinteraksi di dalam aplikasi. Pemilihan pola yang tepat tergantung pada kebutuhan proyek dan kerangka kerja yang digunakan.

## Tugas 3: Implementasi Form dan Data Delivery pada Django
> 1. Apa perbedaan antara form POST dan form GET dalam Django?

Dalam form POST, data dikirimkan dalam tubuh permintaan HTTP, yang berarti data tidak terlihat dalam URL. Hal ini cocok untuk mengirim data yang bersifat rahasia atau sensitif karena tidak mudah dilihat oleh pengguna. Form POST lebih cocok untuk pengiriman data sensitif seperti kata sandi atau informasi pribadi. Pada form POST, tidak ada batasan praktis pada panjang data yang dapat dikirimkan menggunakan metode POST. Penggunaannya form POST adalah untuk mengirim data yang akan diolah oleh server, seperti mengirim formulir, mengirim permintaan AJAX, atau membuat perubahan di server (seperti menambahkan, mengedit, atau menghapus data).

Pada form GET, data dikirimkan sebagai bagian dari URL. Data muncul di dalam string query URL dan dapat dilihat oleh semua orang yang melihat URL tersebut. Ini cocok untuk permintaan yang tidak memiliki efek samping dan hanya membaca data. Form GET menjadi pilihan yang tidak aman apabila ingin mengirim data sensitif. Pada form GET juga terdapat batasan pada panjang URL yang dapat ditangani oleh browser dan server, sehingga tidak cocok untuk mengirim data yang sangat besar. Metode GET digunakan untuk mengambil data dari server, seperti menampilkan halaman web, pencarian, atau mengirim parameter dalam URL.

Referensi:
https://www.w3schools.com/tags/ref_httpmethods.asp 

> 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
1. XML (eXtensible Markup Language)
XML menggunakan sintaksis yang ketat dan deklarasi struktur data dalam bentuk tag untuk mendefinisikan elemen dan hierarki. Format ini digunakan dalam berbagai aplikasi, termasuk konfigurasi, pertukaran data, SOAP (Simple Object Access Protocol) dalam layanan web, dan lain-lain. XML memiliki dukungan yang kuat untuk validasi skema, komentar, dan metadata.

2. JSON (JavaScript Object Notation)
JSON digunakan untuk pertukaran data dan representasi struktur data seperti XML, tetapi dalam format yang lebih ringkas dan mudah dibaca oleh manusia dan diproses oleh mesin. JSON menggunakan format yang lebih ringkas dengan objek yang mudah dibaca dan dihasilkan oleh banyak bahasa pemrograman. Format JSON digunakan dalam berbagai aplikasi, termasuk RESTful API, komunikasi antara server dan klien web, konfigurasi, dan pertukaran data antar bahasa pemrograman. JSON tidak memiliki dukungan untuk validasi skema seperti XML, tetapi itu membuatnya lebih sederhana dan efisien dalam penggunaan sehari-hari.

3. HTML (Hypertext Markup Language)
HTML digunakan untuk membuat tampilan halaman web dan menentukan bagaimana elemen-elemen tampil di browser web. HTML menggunakan sintaksis mirip XML, berisi tag yang mendefinisikan elemen-elemen seperti judul, paragraf, gambar, dan tautan dalam sebuah dokumen web. HTML memiliki kemampuan untuk membuat tampilan grafis yang interaktif di browser dan sering digunakan bersama dengan CSS (Cascading Style Sheets) dan JavaScript untuk membuat pengalaman pengguna yang kaya di web.

> 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan, yaitu:
- Sintaksis JSON mudah dibaca oleh manusia dan ringkas
- JSON memiliki ukuran data yang kecil, sehingga mengurangi beban jaringan
- Bisa digunakan dengan hampir semua bahasa pemrograman
- Mendukung data bersarang dan struktur data kompleks
- Mendukung pembaruan parsial, efisien dalam penggunaan bandwidth
- Standar dalam desain RESTful API, memudahkan integrasi antar layanan web
- Dokumentasi JSON tersedia di banyak bahasa, sehingga memudahkan pengembangan

> 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.

- [x] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

- [x] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.

- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. HTML
![HTML format](html.jpg)

2. XML
![XML format](xml.jpg)

3. JSON
![JSON format](json.jpg)

4. XML by ID
![XML by ID format](xml_by_id.jpg)

5. JSON by ID
![JSON by ID format](json_by_id.jpg)

- [x] Melakukan `add`-`commit`-`push` ke GitHub.