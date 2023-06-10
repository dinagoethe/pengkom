# Pembahasan Problem 1
# Penawaran barang

# Alternatif 1
hargaBarangA = int(input("Masukkan harga dasar barang A : "))
hargaJualA = int(input("Masukkan harga jual barang A : "))
hargaBarangB = int(input("Masukkan harga dasar barang B : "))
hargaJualB = int(input("Masukkan harga jual barang B : "))
hargaBarangC = int(input("Masukkan harga dasar barang C : "))
hargaJualC = int(input("Masukkan harga jual barang C : "))

keuntunganA = hargaJualA - hargaBarangA
keuntunganB = hargaJualB - hargaBarangB
keuntunganC = hargaJualC - hargaBarangC

if keuntunganA > keuntunganB and keuntunganA > keuntunganC:
    barangTawarkan = "A"
elif keuntunganB > keuntunganA and keuntunganB > keuntunganC:
    barangTawarkan = "B"
else:
    barangTawarkan = "C"

print("Barang yang harus ditawarkan adalah barang", barangTawarkan)