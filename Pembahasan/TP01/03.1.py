# Problem 3 : Mengetahui durasi aktivitas dari waktu awal dan waktu akhir

print("Masukkan waktu mulai!")
jam_mulai = int(input("Jam : "))
menit_mulai = int(input("menit : "))
detik_mulai = int(input("detik : "))

print("Masukkan waktu selesai!")
jam_selesai = int(input("Jam : "))
menit_selesai = int(input("menit : "))
detik_selesai = int(input("detik : "))

# konversi ke detik
detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
detik_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

# hitung selisih 
selisih = detik_selesai - detik_mulai

# konversi ke jam, menit, detik
jam = selisih // 3600
menit = (selisih % 3600) // 60
detik = (selisih % 3600) % 60

# cetak hasil
print("Tuan Riz berlari selama ", end="")

if jam > 0:
    print(jam, "jam", end="")
if menit > 0:
    print(menit,"menit", "", detik, "detik")
else:
    print(detik, "detik")