## Program Lalu Lintas Satu Ruas Jalan dengan Penyebrangan

```
# Tugas Besar Pengenalan Komputasi 
# Program lalu Lintas Sederhana
"""
1. Melviza Tsabita Maharani (166222147)
2. Alika Nandina (16622162)
3. Siti Ramadina G.K. (16622212)
4. Fatimah Az-Zahra (16622277)	
5. Vindira Kayla Pualani (16622297)
"""

# Impor modul waktu
import time

# Mendefinisikan waktu dengan array (detik)
# Waktu untuk lampu merah dan hijau 
N = 60
T = [i for i in range(N, 0, -1)]

# Waktu untuk lampu kuning
n = 5
t = [i for i in range(n, 0, -1)]

# Waktu untuk pejalan kaki menyebrang
p = 10
w = [i for i in range(p, 0, -1)]

# Waktu untuk pejalan kaki menunggu pergantian lampu penyebrangan
q = 3
s = [i for i in range(q, 0, -1)]

# Mencacah mundur waktu dengan subprogram
# Untuk lampu merah dan hijau
def lampu(RG):
    for i in T: 
            print(i)
            time.sleep(1)

# Untuk lampu kuning
def siapHijau(G):
    print("Siap-siap lampu hijau..")
    for i in t:
        print(i)
        time.sleep(1)

# Untuk lampu kuning ketika akan berubah merah
def siapMerah(R):
    print("Sebentar lagi lampu merah...!")
    for i in t:
        print(i)
        time.sleep(1)

# Untuk pejalan kaki ketika menyebrang di tengah waktu lampu hijau berjalan
def pejalanKaki(orang):
    for i in w:
        print(i)
        time.sleep(1)

def nungguBentar(orang):
    for i in s:
        print(i)
        time.sleep(1)

"""
print("Tekan 1 saat lampu hijau menyala")
G1 = int(input("Kondisi lampu hijau: "))
"""


G1 = 1  # Asumsi di awal kondisi lampu hijau menyala
# Program lampu lalu lintas dijalankan
while True:
    try:
        while G1 == 1:
            print("Lampu hijau menyala. Kendaraan jalan!")
            lampu(G1)
            siapMerah(G1)
            print("Lampu merah menyala. Kendaraan berhenti!")
            lampu(G1)
            siapHijau(G1)

# Interupsi pejalan kaki yang mau menyebrang
    except KeyboardInterrupt:
        pass
        print("Ayo siap-siap berhenti! Ada pejalan kaki mau menyebrang")
        print("Pejalan kaki harap tunggu sebentar")
        nungguBentar(G1)
        print("Lampu merah menyala. Kendaraan berhenti.")
        print("Silakan menyebrang! Semoga selamat sampai tujuan...")
        pejalanKaki(G1)
        G1 == 1
        print("Lampu hijau kembali menyala.")
        print("Berhenti menyebrang.")

"""
# Melakukan perulangan lampu lalu lintas
while G1>= 0:
    # Ketika hijau pertama menyala
    if G1 == 1:
        print("Jalan!")
        lampu(G1)
        siapMerah(G1)
        print("Berhenti!")
        lampu(G1)
        siapHijau(G1)

    # Ketika merah pertama menyala
    if G1 == 0:
        print("Berhenti")
        lampu(G1)
        siapHijau(G1)
        print("Jalan!")
        lampu(G1)
        siapMerah(G1)
"""
```
