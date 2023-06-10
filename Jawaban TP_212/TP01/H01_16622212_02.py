# NIM/Nama : 16622212/Siti Ramadina Goethe K.
# Tanggal : 15/09/2022, 03:20 - 4:14 WIB
# Problem 2 (Pengelompokkan kelas berdasarkan NIM)

"""
Di setiap rentang NIM, akan dicari bilangan yang habis dibagi 2 untuk menentukan bilangan genap melalui
if percabangan, sedangkan sisanya diartikan sebagai bilangan ganjil.

Bilangan m yang habis dibagi 2 dicari menggunakan modulo (%) yang hasil operasinya akan bernilai 0.
Contoh :
    4 dibagi 2 habis terbagi = 0
    5 dibagi 2 ada sisanya, yaitu 1
"""
m = int(input("Masukkan akhiran NIM : "))

if (1<=m<=100):                                 # Mahasiswa dengan NIM 001 sampai dengan 100
    if (m % 2 == 0):                            # Di dalam if ada percabangan lagi
        print("Mahasiswa masuk ke kelas K2")    
    else:                                       # NIM yang tak memenuhi syarat if akan mengikuti perintah else
        print("Mahasiswa masuk ke kelas K1")
elif (101<=m<=200):                             # Mahasiswa dengan NIM 101 sampai dengan 200
    if (m % 2 == 0):                            # NIM genap
        print("Mahasiswa masuk ke kelas K4")
    else:                                       # NIM ganjil
        print("Mahasiswa masuk ke kelas K3")
elif (201<=m<=300):                             # Mahasiswa dengan NIM 201 sampai dengan 300
    if (m % 2 == 0):
        print("Mahasiswa masuk kek kelas K6")
    else:
        print("Mahasiswa masuk ke kelas K5")
elif (m>300):                                   # Mahasiswa dengan NIM lebih dari 300
    if (m % 2 == 0):
        print("Mahasiswa masuk ke kelas K8")
    else:
        print("Mahasiswa masuk ke kelas K7")
    

