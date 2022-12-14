# Revisi Tugas Besar Pengkom

Dari hasil presentasi kelompok kami tanggal `01/11/2022, 15.30 WIB`, terdapat beberapa masukkan dari dosen untuk merevisi program kami. 
Program lampu lalu lintas kami perlu ditambahkan masalah yang lebih kompleks seperti hal-hal sebagai berikut:
1. Persimpangan 4 ruas jalan
2. Lampu giliran penyebrangan untuk pejalan kaki
3. Panjang pendeknya waktu bergantung dari kondisi jalan (Opsional kalau bisa)
4. Mendeteksi kemacetan (ini sudah diluar kemampuan lampu lalin, sudah masuknya program lain yang membutuhkan sensor)

Pemisahan program perlu dilakukan agar memudahkan penulisan program: 

**1. Fase 1:** Satu ruas jalan (**done**, [source code](https://github.com/dinagoethe/pengkom/blob/main/tb/program_jadi.md))

**2. Fase 2:** Penyebrangan pejalan kaki (**done**, [source code](https://github.com/dinagoethe/pengkom/blob/main/tb/revisi/programjadi_penyebrangan.md))

**3. Fase 3:** Persimpangan (**done**, [source code](https://github.com/dinagoethe/pengkom/blob/main/tb/revisi/persimpangan.md))

## Deskripsi dan alur masalah baru:
**1. Penyebrangan** 
  - Memberhentikan sejenak loop lampu lalu lintas yang sudah berjalan
  - Menunggu sejenak pergantian lampu penyebrangan
  - Menghitung mundur waktu pejalan kaki menyebrang 
  - Kembali ke loop utama 
  - Program dapat diinterupsi kembali saat lampu hijau

**2. [Persimpangan](https://github.com/dinagoethe/pengkom/blob/main/tb/revisi/pseudo_persimpangan.md)**
  - Membuat animasi persimpangan (jika bisa)
  - Menentukan ruas jalan yang mana saja yang sedang berjalan atau tidak

## Dekomposisi masalah baru
| Masalah | Ide penyelesaian | Referensi |
| ------- | ---------------- | --------- |
| Pergantian nyala lampu setiap persimpangan | menggunakan matriks (array) dan tabel |[Python-Matrix](https://www.tutorialspoint.com/python_data_structure/python_matrix.htm)
| Kondisi kendaraan pada setiap nyala lampu | menggunakan *if conditional* ||
| Lama lampu menyala, hitung mundur | menggunakan *countdown timer* atau pencacahan mundur dengan mengimpor `import time` | [How To Create a Countdown Timer Using Python?](https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/) |
| Agar lampu lalin tetap berjalan terus | menggunakan looping | [Ref](https://github.com/dinagoethe/pengkom/blob/main/tb/source.md); [Traffic light program using while loop in python](https://stackoverflow.com/questions/48197670/traffic-light-program-using-while-loop-in-python) |
| Giliran penyebrangan untuk pejalan kaki | menggunakan perintah `keyboardInterrupt` dan CTRL+C | [Python: how to interrupt, then return to while loop, without goto?](https://stackoverflow.com/questions/33273930/python-how-to-interrupt-then-return-to-while-loop-without-goto)

## Pembagian Tugas Presentasi Video
| Slide | Materi | Presenter |
| ----- | ------ | --------- |
| | Intro | `SR` |
| | Perkenalan | semua |
| | Latar Belakang | |
| | Tujuan | | 
| | Fungsi lampu lalin | `FA` | 
| | Dekomposisi Masalah | `SR` |
| | Flowchart | |
| | Program Bagian 1 (penyebrangan pada 1 ruas jalan) | `SR` |
| | Simulasi Bagian 1 | `SR` |
| | Program Bagian 2 (persimpangan) | `SR` |
| | Simulasi Bagian 2 | `SR` |
| | Kesimpulan | |
| | *Lesson Learned* atau kesan pesan | |
| | Outro | `SR` |
