# NIM/Nama : Siti Ramadina Goethe K.
# Tanggal : 15/09/2022, 11.30 - 20:47 WIB
# Problem 1 (Menentukan barang yang akan ditawarkan berdasarkan keuntungan)

# Memasukkan data harga dasar (x) dan harga jual (y)
xA = int(input("Masukkan harga dasar barang A : "))
yA = int(input("Masukkan harga jual barang A : "))

xB = int(input("Masukkan harga dasar barang B : "))
yB = int(input("Masukkan harga jual barang B : "))

xC = int(input("Masukkan harga dasar barang C : "))
yC = int(input("Masukkan harga jual barang C : "))


# Menghitung keuntungan yang diperoleh
"""
keuntungan (z) = harga jual (y) - harga dasar (x)
"""
zA = yA-xA; print("Keuntungan barang A adalah", zA)
zB = yB-xB; print("Keuntungan barang B adalah", zB)
zC = yC-xC; print("Keuntungan barang C adalah", zC)

# Membandingkan keuntungan untuk mendapatkan barang yang ingin ditawarkan
if (zA>zB and zA>zC):                               # Ketika A lebih besar dari B dan C
    print("Barang yang harus ditawarkan adalah A")

elif (zB>zA and zB>zC):                             # Ketika B lebih besar dari A dan C
    print("Barang yang harus ditawarkan adalah B")

else:                                               # Ketika C lebih besar dari A dan B
    print("Barang yang harus ditawarkan adalah C")


