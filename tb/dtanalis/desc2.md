# Tugas Besar 2 Pengkom 2022
`Topik : Data Analisis`

## Sumber Data
1. [Data Timbulan Sampah](https://docs.google.com/spreadsheets/d/1eu4DChuI-Z_LJTgsH58Yt-Y6GNf3EO8E/edit?usp=share_link&ouid=102172680674629401624&rtpof=true&sd=true)
2. [Data Komposisi Jenis Sampah](https://docs.google.com/spreadsheets/d/15SM4u2lZewoC8J5A5VG4IGOpbUC4zA2P/edit?usp=share_link&ouid=102172680674629401624&rtpof=true&sd=true)
3. [Data Komposisi Sumber Sampah](https://docs.google.com/spreadsheets/d/1B7xMx9-5Q4eOmw8Vp4-KzMG2MAzuIZa5/edit?usp=share_link&ouid=102172680674629401624&rtpof=true&sd=true)

Deskripsi singkat: data yang digunakan tentang penimbunan sampah dan jenisnya dalam skala nasional selama rentang waktu 4 tahun (2018-2021).
Ketentuan data: 
- Minimal 5 kolom
- Minimal 60 baris
- Mengandung atribut kategorikal dan kuantitatif
- Salah satu kolom nya ada data waktu (*time series*)

Referensi sumber: 
- [BPS](https://www.bps.go.id/)
- [Data market](https://www.qlik.com/us/products/qlik-sense/data-sources)
- [Satu Data Indonesia](https://data.go.id/home)

## Deskripsi
Apa yang ingin diketahui dari data tsb?
1. [Data Timbulan Sampah](https://github.com/dinagoethe/pengkom/blob/main/tb/dtanalis/timbulan.md)
2. [Data Komposisi Jenis Sampah]()
3. [Data Komposisi Sumber Sampah]()


### 3. Tentang data

Tentang data | Jawab
| ------ | -----|
Format data |
Kolom | 
Baris | 
Ukuran file |
Tool | Jupyter-notebook & pandas

### 4. Bagaimana mengetahui berbagai informasi yang terkait dengan data?

### 5. Atribut


| Nama atribut | Jenis | |Karakteristik | Sintaks/bahasa pemrograman | Penjelasan |
| ------------ | ----- | -------------- | -------------------------- | ---------- |
| Tahun | kuantitatif | range? persen data yg kosong? | sorting, exremum, dll. |  |

### 6. Statistik
- Rata-rata
- Standar deviasi
- Percentile (10%, 25%, 50%, 75%, 90%)
- Ekstremum (nilai maksimum dan minimum)
- Distribusi frekuensi nilai pada data
- Informasi/pengetahuan yang bisa didapatkan dari statistik tersebut.

 Sampel data
- Data baris pertama
- Data terbesar dan terkecil (sort)
- Sampel data tiap kolom


### 7. Visualisasi
- Grafik/chart masing-masing minimum 2
buah, untuk setiap kategori berikut:
  - Perbandingan kategori
  - Penampilan perubahan terhadap waktu
  - Penampilan hierarki dan hubungan keseluruhan-bagian
  - Plotting relationships
- Untuk tiap visualisasi yang dibuat dilengkapi visualisasi dengan informasi penting:
  - label sumbu x dan y
  - legenda dan
  - Judul visualisasi. 
- Bonus: penggunaan warna
- Insight yang didapat dari visualisasi
- Sintaks pemrograman setiap visualisasi
- Korelasi
  - antar semua atribut kuantitatif
  - angka dan grafik terkait
  - sintaks korelasi dan visualisasinya 

### 8. Data cleansing - Bonus
• Bonus: Jika data Anda dalam keadaan “kotor”, yaitu mengandung
terlalu banyak data kosong atau data yang salah (misalnya: data
umur seharusnya > 0, tetapi pada data terdapat angka negatif),
buatlah pembahasan khusus tentang:
• Deskripsi tentang tingkat kekotoran data, misalnya: pada atribut yang mana,
berapa persen data yang kotor, dll.
• Bagaimana Anda mengatasinya:
• Jika dibiarkan apa adanya, jelaskan apa alasannya.
• Jika “dibersihkan”, jelaskan apa alasannya dan bagaimana melakukannya: apakah
diubah nilainya, atau dihapus baris yang mengandung data kotor, dll.
• Tuliskan dengan bahasa pemrograman/spreadsheet tool bagaimana
untuk mengecek “kekotoran data” dan bagaimana melakukan
pembersihan data (jika dilakukan).

