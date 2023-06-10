# NIM/Nama  : 16622212/Siti Ramadina G.K.
# Tanggal   : 4/11/2022
# Deskripsi : Program Pemotretan gedung

# KAMUS
"""
M, N: int
kosong: array of int
foto: array of int
"""

"""
# Tampak gedung dari atas
def dari_atas(x, kolom):
    M = len(x)     # banyak nilai pada baris
    N = len(x[0])  # banyak nilai pada kolom
    kosong = []
    for baris in range(M):
        if baris == 0:
            kosong.append(x[baris][kolom])
        else:
            if x[baris][kolom] > kosong[len(kosong) - 1]:
                kosong.append(x[baris][kolom])
    return kosong

# Tampak gedung dari bawah
def dari_bawah(x, kolom):
    M = len(x)     # banyak nilai pada baris
    N = len(x[0])  # banyak nilai pada kolom
    kosong = []
    for baris in range(M-1, -1, -1):
        if baris == M-1:
            kosong.append(x[baris][kolom])
        else:
            if x[baris][kolom] > kosong[len(kosong) - 1]:
                kosong.append(x[baris][kolom])
    return kosong

# Foto
foto = [
    [3, 1, 5],
    [6, 8, 2],
    [1, 3, 4]
]

l1 = dari_atas(foto, 0)
l2 = dari_atas(foto, 1)
l3 = dari_atas(foto, 2)

l4 = dari_bawah(foto, 0)
l5 = dari_bawah(foto, 1)
l6 = dari_bawah(foto, 2)

l = [l1, l2, l3, l4, l5]
for i in l:
    print(i)

h = [sum(i) for i in l]
h_maks = max(h)
print("Foto terbaik memiliki total tinggi", h_maks)


foto = [
    [10, 5, 7, 1],
    [12, 10, 13, 12],
    [10, 5, 4, 3],
    [1, 1, 11, 12]
]

l1 = dari_atas(foto, 0)
l2 = dari_atas(foto, 1)
l3 = dari_atas(foto, 2)
l4 = dari_atas(foto, 3)

l5 = dari_bawah(foto, 0)
l6 = dari_bawah(foto, 1)
l7 = dari_bawah(foto, 2)
l8 = dari_bawah(foto, 3)

l = [l1, l2, l3, l4, l5, l6, l7, l8]
for i in l:
    print(i)

h2 = [sum(i) for i in l]
h_maks2 = max(h2)
print("Foto terbaik memiliki total tinggi", h_maks2)
"""


M = int(input("Masukkan besar Kota Kompeng: "))
N = M

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
    
h2 = [sum(i) for i in M]
h_maks2 = max(h2)
print("Foto terbaik memiliki total tinggi", h_maks2)