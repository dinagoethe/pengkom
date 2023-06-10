# NIM/Nama : 16622212/Siti Ramadina G.K.
# Tanggal : 07/10/2022
# Problem 2 : Penjumlahan Angka yang Membesar

# num = [1, 5, 3, 2, 3, 4, 4, 4, 3]
# num = [-3, -2, -1, 6, 1, 0, -1] 

# Jumlah bilangan yang diinginkan
print("Masukkan banyak bilangan:", end="")
N = int(input())
num = [0]*N

print(num)

# Memasukkan bilangan sebanyak N
for i in range(N):
    print("Bilangan ke-", i+1,":", end="")
    num[i] = int(input())

print("List bilangan: ", num)

# Jumlah tiga bilangan yang membesar
j = 0 

for i in range(1, len(num)): # len(num) adalah banyaknya bilangan yg telah dimasukkan (N)
    k = num[i] - num[i-1]
    if(k > 0):
        j = j + num[i]

print("Penjumlahan nilai yang membesar adalah", j)