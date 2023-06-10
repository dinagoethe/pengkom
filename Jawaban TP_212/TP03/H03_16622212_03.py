# NIM/Nama : 16622212/Siti Ramadina G.K.
# Tanggal : 21/10/2022
# Deskripsi : Program menghitung banyak kemunculan sebuah string

# KAMUS
"""
Tipe data:
L1, L2 : integer
str1, str2 : string
N : integer
h1, h2, h3, h4 : char
"""
# str1 = [t,u,a,n]
# str1[0] = t, str1[1] = u, str1[2] = a, str1[3] = n

# Meminta masukan data berupa panjang string dan stringnya
L1 = int(input("Masukkan panjang string 1: "))
str1 = (input("Masukkan string 1: "))

L2 = int(input("Masukkan panjang string 2: "))
str2 = (input("Masukkan string 2: "))

# Mengecek setiap char pada string 1 mirip dengan pada string 2
N = 0
for i in range(L2-L1+1):
    h1 = str1[0] == str2[i]
    h2 = str1[1] == str2[i+1]
    h3 = str1[2] == str2[i+2]
    h4 = str1[3] == str2[i+3]
    if h1 and h2 and h3 and h4:
        N = N + 1

print("String 1 muncul sebanyak", N, "kali")
