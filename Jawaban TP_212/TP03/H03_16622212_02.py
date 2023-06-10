# NIM/Nama : 16622212/Siti Ramadina G.K.
# Tanggal : 20/10/2022
# Deskripsi : Program kondisi nyala lampu

# KAMUS
"""
Tipe variabel:
X, Y, integer, btn : integer
lam : array

Arti variabel:
X = banyak lampu
Y = banyak tekan
lam = daftar lampu
btn = tekan ke-
"""

X = int(input("Masukkan banyak lampu:"))
lam = X*[0]

Y = int(input("Masukkan berapa kali Tuan Kil menekan tombol:"))

# Tombol yang ditekan ke-n
for j in range(Y):
    # btn = int(input("Tombol yang ditekan ke"))
    print("Tombol yang ditekan ke-", j+1, ":", end="")
    btn = int(input())

    i = btn - 1
    lam[i] = 1 - lam[i]

# Mengecek kondisi nyala lampu
    if btn == 1:
        lam[i + 1] = 1 - lam[i + 1]
    elif btn == X:
        lam[i - 1] = 1 - lam[i - 1]
    else:
        lam[i + 1] = 1 - lam[i + 1]
        lam[i - 1] = 1 - lam[i - 1]

print("Keadaan akhir rangkaian lampu adalah", lam)