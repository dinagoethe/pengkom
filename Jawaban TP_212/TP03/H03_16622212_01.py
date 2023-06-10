# NIM/Nama : 16622212/Siti Ramadina G.K.
# Tanggal : 20/10/2022
# Deskripsi : Bot mencari diskon barang yang paling besar

# KAMUS :
"""
Tipe data :
N, h, p, d, dmaks: integer

Arti variabel :
h = daftar harga barang
p = daftar persen diskon
d = diskon
dmaks = diskon terbesar

"""
# Daftar kosong barang
N = int(input("Masukkan banyak barang: "))
h = N*[0]                       # List kosong sebanyak N

# Loop harga awal barang ke-
for x in range(N):
    print("Masukkan harga awal barang ke-", x+1, ":", end="")
    h[x] = int(input())

# Daftar kosong persen diskon
p = N*[0]
# Loop persen diskon barang ke-
for y in range(N):
    print("Masukkan persen diskon barang ke-", y+1, ":", end="")
    p[y] = int(input())

# Mencari diskon tiap barang
# diskon = harga_awal * persen_diskon
idx = -1
for i in range(N):
    j = i + 1
    d = h[i]*p[i]/100

# Membandingkan harga barang setelah didiskon
    if i == 0:
        dmaks = d
        idx = j
    else:
        if d > dmaks:
            dmaks = d
            idx = j

print("Barang", idx, "memiliki diskon paling besar yaitu", dmaks)