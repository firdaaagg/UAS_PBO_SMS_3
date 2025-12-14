Aplikasi Pendataan Mahasiswa (UAS PBO)

Repository ini berisi project Ujian Akhir Semester (UAS) mata kuliah Pemrograman Berorientasi Objek (PBO). Project yang dibuat berupa aplikasi pendataan mahasiswa berbasis GUI menggunakan bahasa pemrograman Python dengan library Tkinter.
Aplikasi ini digunakan untuk mengelola data mahasiswa secara sederhana, meliputi penambahan data, pengeditan data, penghapusan data, pencarian data, serta export data ke file CSV. Pembuatan aplikasi ini juga bertujuan untuk menerapkan konsep-konsep dasar Object Oriented Programming (OOP) yang telah dipelajari selama perkuliahan.

Beberapa fitur utama yang terdapat pada aplikasi ini antara lain:

1. Menampilkan daftar data mahasiswa
2. Menambahkan data mahasiswa reguler
3. Menambahkan data mahasiswa transfer
4. Mengedit data mahasiswa
5. Menghapus data mahasiswa
6. Pencarian data berdasarkan NIM, Nama, Kelas, Program Studi, dan Tahun Masuk
7. Export data mahasiswa ke dalam format CSV

Aplikasi ini menerapkan beberapa konsep Pemrograman Berorientasi Objek, yaitu:

1. Class dan Object untuk merepresentasikan data mahasiswa
2. Inheritance, dengan class Mahasiswa sebagai class induk dan MahasiswaReguler serta MahasiswaTransfer sebagai class turunan
3. Encapsulation, melalui penggunaan attribute dan method getter-setter
4. Polymorphism, pada method display_info() yang dioverride pada class turunan

Teknologi yang Digunakan

Bahasa Pemrograman : Python
Library GUI : Tkinter
Format Penyimpanan Data : CSV dan Spreadsheet (Excel)

Struktur file dalam repository ini adalah sebagai berikut:

1. uas_pbo_mahasiswa.py : File utama program aplikasi
2. data_mahasiswa_final.xlsx : Data mahasiswa dalam bentuk spreadsheet
3. DIAGRAM UAS PBO.drawio : Diagram perancangan sistem
4. Image Dokumentasi/ : Screenshot hasil pengujian aplikasi
5. 032_Firda Agustina_2024B_LAPORAN UAS PBO.pdf : Laporan UAS PBO

Cara Menjalankan Program

* Pastikan Python sudah terinstall di komputer
* Buka folder project ini
* Jalankan file berikut melalui terminal atau IDE:
* python uas_pbo_mahasiswa.py
* Aplikasi pendataan mahasiswa akan muncul dalam bentuk GUI

Catatan

Project ini dibuat untuk keperluan tugas UAS Pemrograman Berorientasi Objek dan masih dapat dikembangkan lebih lanjut, baik dari sisi tampilan maupun penyimpanan data berbasis database.

Penutup

Dengan adanya aplikasi ini, diharapkan dapat membantu proses pengelolaan data mahasiswa secara lebih terstruktur sekaligus menjadi sarana pembelajaran dalam menerapkan konsep PBO pada aplikasi nyata berbasis GUI.
