# Pembahasan Tugas Pendahuluan
# Problem 1 : Penawaran barang

# Alternatif 2
hargaDasar = int(input("Masukkan harga dasar barang A: "))
hargaJual= int(input("Masukkan harga jual barang A: "))

keuntunganMaks = hargaJual - hargaDasar
barangTawarkan = "A"

hargaDasar = int(input("Masukkan harga dasar barang B: "))
hargaJual= int(input("Masukkan harga jual barang B: "))

keuntungan= hargaJual - hargaDasar

if keuntungan > keuntunganMaks:
    keuntunganMaks = keuntungan
    barangTawarkan = "B"

hargaDasar = int(input("Masukkan harga dasar barang C: "))
hargaJual= int(input("Masukkan harga jual barang C: "))

keuntungan= hargaJual - hargaDasar

if keuntungan > keuntunganMaks:
    keuntunganMaks = keuntungan
    barangTawarkan = "C"

print("Barang yang harus ditawarkan adalah barang", barangTawarkan)