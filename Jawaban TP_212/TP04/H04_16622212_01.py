# NIM/Nama  : 16622212/Siti Ramadina G.K.
# Tanggal   : 3/11/2022
# Deskripsi : Program Penumpukan Barang

# KAMUS
"""
M, N: int
X: array of int
"""
M = int(input("Masukkan tinggi tumpukan: "))
N = int(input("Masukkan banyak tumpukan: "))

# Mendeklarasi matriks
X = [[0 for j in range(N)] for i in range(M)]

# Memasukkan input pada matriks X[baris][kolom]
for i in range(M):
    for j in range(N):
        X[i][j] = int(input("Masukkan berat benda pada baris ke-"+str(i+1)+" kolom ke-"+str(j+1)+": "))

for i in range(M):
    for j in range(N):
        print(X[i][j], end="")
    print("")

# Membandingkan berat benda paling bawah dengan benda yang berada di atasnya
if X[M-2][N-2] < X[M-1][N-1]: # Karena matriks sama seperti array, dimulai dari nol dan berakhir M-1/N-1
    print("Susunan tersebut memenuhi perintah Tuan Leo")
else:
    print("Susunan tersebut tidak memenuhi perintah Tuan Leo")

