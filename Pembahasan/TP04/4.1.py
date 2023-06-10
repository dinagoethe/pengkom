# Program akan menerima suatu susunan dan mengecek apakah susunan memenuhi perintah

# KAMUS
# tumpukan  : array of integer
# cek       : bool

t = int(input('Masukkan tinggi tumpukan: '))
n = int(input('Masukkan banyak tumpukan: '))

# Input array 2 dimensi
tumpukan = [[0 for j in range(n)] for i in range(t)] # Inisialisasi array
for i in range(t):
    for j in range(n):
        tumpukan[i][j] = int(input(f"Masukkan berat benda pada baris ke-{i+1} kolom ke-{j+1}: "))

# Cek susunan dengan asumsi awal tumpukan terbawah nilai tertinggi
cek =True
for j in range(n):
    for i in range(t-1):
        if tumpukan[i][j] > tumpukan[t-1][j]:
            cek = False

# Output hasil
if cek:
    print('Susunan tersebut memenuhi perintah Tuan Leo')
else:
    print('Susunan tersebut tidak memenuhi perintah Tuan Leo')