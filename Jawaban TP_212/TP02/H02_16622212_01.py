# NIM/Nama : 16622212/Siti Ramadina G.K.
# Tanggal : 06/10/2022
# Problem 2 : Bilangan Sempurna

"""
Test Case 1 :
Masukkan bilangan : 28
Bilangan tersebut adalah bilangan sempurna

Test Case 2 : 
Masukkan bilangan : 15
Bilangan tersebut bukan bilangan sempurna
"""

# Masukkan bilangan yang akan dicek
n = int(input("Masukkan bilangan : "))
m = 0

# Mengecek faktor dari bilangan n
for i in range(1, n):
    if (n % i == 0):
        m = m + i   # Menjumlahkan faktor

# Mengecek bilangan sempurna
if m == n:
    print("Bilangan tersebut adalah bilngan sempurna") 
else:
    print("Bilangan tersebut bukan bilangan sempurna")
