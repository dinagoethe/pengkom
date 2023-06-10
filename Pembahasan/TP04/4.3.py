# Program akan menerima nilai tinggi kumpulan bangunan dan mengeluarkan nilai tertinggi bangunan yang terlihat pada suatu kolom

# KAMUS
"""
gedung      : array of integer
n, maks     : int
pointer     : int
atas, bawah : int
"""

# ALGORITMA
n = int(input('Masukkan besar Kota Kompeng: '))

# Input array dua dimensi
gedung = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        gedung[i][j] = int(input(f'Masukkan tinggi bangunan bari ke-{i+1} kolom ke-{j+1}: '))

# Mencari nilai tertinggi 
maks = 0
for j in range(n):      # Mengecek tiap kolom
    #Dilihat dari depan
    pointer = gedung[0][j]
    atas = pointer
    for i in range(1, n):
        if pointer <= gedung[i][j]:
            pointer = gedung[i][j]
            atas += pointer

    # Dilihat dari belakang
    pointer = gedung[n-1][j]
    bawah = pointer
    for i in range(n-2, -1, -1):
        if pointer <= gedung[i][j]:
            pointer = gedung[i][j]
            bawah += pointer

    # Mengambil nilai maksimum
    if maks < atas:
        maks = atas
    elif maks < bawah:
        maks = bawah

# Output hasil
print('Foto terbaik memiliki total tinggi ', maks)