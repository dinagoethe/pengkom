# NIM/Nama  : 16622212/Siti Ramadina G.K.
# Tanggal   : 3/11/2022
# Deskripsi : Program Pengurangan Nilai

# KAMUS
# N: int
# C: array

# Subprogram fungsi untuk mencari nilai minimum setiap baris array
def minimal(list):
    xmin = max(list)                # Mencari nilai maksimum dalam array/list C
    for i in list:
        if i > 0 and xmin > i:      # Mencacah tiap nilai minimum kecuali 0    
            xmin = i
    return xmin 

# Subprogram funsgi untuk mengurangi bilangan dengan nilai minimum kecuali jika sudah 0
def kurangi(x, min_x):                # dengan x: array dan num: bilangan minimum dari array tsb.
    if x > 0:
        x = x - min_x
    return x

N = int(input("Masukkan banyak nilai: "))
C = [int(input("Masukkan nilai ke-"+str(i+1)+": ")) for i in range(N)]
print(C)

for i in range(N):
    min_C = minimal(C)
    for j in range(N):
        C[j] = kurangi(C[j], min_C)
    print(C)



"""
i = 4 --> xmin = 6 --> 6 > 4 --> 4
i = 2 --> xmin = 4 --> 2
i = 1 --> xmin = 2 --> 1
"""