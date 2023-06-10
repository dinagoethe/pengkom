# Program akan menerima banyak nilai dan melakukan prosedur pengurangan dengan nilai terkecil

# KAMUS
"""
cek_nol()   : function
cari_min()  : function
arr         : array of integer
cek         : bool
maks,min    : int
n, kurangin : int

"""

# ALGORITMA
def cek_nol(arr, n):        # Fungsi mengecek kumpulan nilai sudah nol
    cek = True              # Asumsi awal semua bernilai nol
    for i in range(n):
        if arr[i] != 0:
            # Apabila ada yang tidak nol, asumsi awal menjadi salah
            cek = False

        return cek
    
def cari_min(arr, n):       # Fungsi mencari nilai terkecil yang bukan nol
    # Mencari nilai terbesar dahulu agar tidak terjadi looping terus-menerus
    maks = arr[0]
    for i in range(1, n):
        if arr[i] > maks:
            maks = arr[i]

    # Mencari nilai terkecil yang bukan nol
    min = maks
    for i in range(n):
        if arr[i] < min and arr[i] != 0:
            min = arr[i]

    return min

# Input
n = int(input('Masukkan banyak nilai: '))

# Input array of integer
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(input(f'Masukkan nilai ke-{i+1}: '))


while not(cek_nol(arr, n)):     # Looping selama semua tidak nol
    # Print kondisi array
    for i in range(n):
        print(arr[i], end='')
    print()

    # Prosedur mengurangi array dengan nilai terkecil
    kurangin = cari_min(arr, n)
    for i in range(n):
        arr[i] -= kurangin
        if arr[i] < 0:      # Agar tidak nilai negatif
            arr[i] = 0

# Print kondisi akhir (saat semua nilai nol)
for i in range(n):
    print(arr[i], end='')