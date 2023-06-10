# NIM/Nama : Siti Ramadina Goethe K.
# Tanggal : 16/09/2022, 10:49 - 11:54 WIB
# Problem 3 (Mengetahui durasi aktivitas dari waktu awal dan waktu akhir)

# Waktu awal (t)
print("Masukkan waktu awal!")
th = int(input("Masukkan jam : "))
tm = int(input("Masukkan menit : "))  
ts = int(input("Masukkan detik : "))

# Waktu akhir (w)
print("Masukkan waktu akhir!")
wh = int(input("Masukkan jam : "))
wm = int(input("Masukkan menit : "))
ws = int(input("Masukkan detik : "))

# Durasi = waktu akhir (t) - waktu awal (w)
j = wh-th          # jam
m = wm-tm          # menit
d = ws-ts          # detik

# Meminjam satuan menit ketika waktu menunjukkan minus
"""
Ketika satuan waktu menunjukkan angka negatif, maka kita harus menggunakan metode peminjaman pada satuan yang lebih besar.
Misal pada soal menit : 14-55 = -41

Maka harus meminjam 1 (60 menit pada satuan jam)
60 + 14 - 55 = 74 - 55 = 19 menit
"""
if (m<0):           # Ketika menit ada kemungkinan bernilai negatif
    j = j - 1
    m = m + 1 * 60

if (d<0):           # Ketika detik ada kemungkinan bernilai negatif
    m -= 1          # sama seperti m = m - 1
    d += 1 * 60     # sama seperti d = d + 1


# Tidak menampilkan satuan ketika waktu = 0
if (m == 0 and d == 0):
    print("Tuan Riz berlari selama", j, "jam")

elif (j == 0 and d == 0):
    print("Tuan Riz berlari selama", m, "menit")

elif (j == 0 and m == 0):
    print("Tuan Riz berlari selama", d, "detik")

elif (d == 0):
    print("Tuan Riz berlari selama", j, "jam", m, "menit")

elif (j == 0):
    print("Tuan Riz berlari selama", m, "menit", d, "detik")

else :
    print("Tuan Riz berlari selama", j, "jam", m, "menit", d, "detik")

