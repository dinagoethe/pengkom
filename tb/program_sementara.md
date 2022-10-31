Potongan program/psedocode berikut digunakan sementara untuk melengkapi laporan dan ppt.

#### 1. Mendefinisikan array waktu:
```
# Untuk lampu hijau dan merah
N = 60
T = [i for i in range(1, N+1)]

# Untuk lampu kuning
n = 3 
t = [i for i in range(1, n+1)]
```

#### 2. Mendefinisikan subprogram
```
def RedGreen(R1, G1):
    for i in range(T):
        print(i)
    time.sleep(1)

def Yellow(Y1):
    for i in range(T):
        print(i)
    time.sleep(1)
```

#### 3. Memasukkan input
```
R1 = int(input("Masukkan nyala lampu merah: "))
```

**Keterangan:** 
- ON = 1
- OFF = 0

#### 4. Kondisi lampu dan kendaraan
Program utama memanggil subprogram sebelumnya.
```
     if R1 == 1: # Jika yang nyala dari merah dulu
        # lampu merah
        print("Berhenti")
        RedGreen(R1, G1)
        print("siap-siappp")

        # lampu kuning
        Yellow()
        print("Jalan!")

        # lampu hijau
        RedGreen()
        
     if R1 == 0: # Jika yang nyala dari hijau dulu
       # lampu hijau
        print("Jalan!")
        RedGreen()
        print("siap-siappp")

        # lampu kuning
        Yellow()
        print("Jalan!")

        # lampu merah
        RedGreen()
```

#### 5. Melakukan perulangan
```
while R1 >= 0
  do bagian 4 (males nyalin lagi :v)
```

### Progress 9:42
```
import time

N = 5
T = [i for i in range(N, 0, -1)]

n = 3
t = [i for i in range(n, 0, -1)]

def lampu(L):
    if L == 1:
        print("Jalan!")
    elif L == 0:
        print("Berhenti")

def siap(L):
    print("Siap-siap")
    for i in t:
        print(i)
        time.sleep(1)

print("Kondisi lampu:")
print("ON = 1")
print("OFF = 0")
G1 = int(input("Kondisi lampu hijau? "))

while G1>= 0:
    lampu(G1)
    for i in T: 
        print(i)
        time.sleep(1)
    
    print("Bentar lagi lampu merah...!")
    for i in t:
        print(i)
        time.sleep(1)

    print("Berhenti!")
    for i in T: 
        print(i)
        time.sleep(1)

    siap(G1)
  ```
