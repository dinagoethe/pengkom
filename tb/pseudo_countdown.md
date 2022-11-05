### Alur program:
1. Mendefinisikan array dari waktu:
    - lampu merah/hijau: T = [60,59,58,...0]
    - lampu kuning: t = [3,2,1]
2. Mendefinisikan subprogram
    - Pencacahan mundur waktu lampu merah menggunakan rentang array yang telah diketahui sebelumnya.
    - Pencacahan mundur waktu lampu kuning menggunakan rentang array yang telah diketahui sebelumnya.
    - Pencacahan mundur waktu lampu hijau menggunakan rentang array yang telah diketahui sebelumnya.
```
# Untuk lampu merah/hijau
def RedGreen(R)
for i in T:
    print(i)
    time.sleep(1)

# Untuk lampu kuning
def Yellow2(Y):
for i in t:
    print(i)
    time.sleep(1)

```

3. Program utama
    - Input: Meminta masukkan nyala lampu hijau: 1 (on) atau 0 (off)
    - If else:
```
if R1 == 1:
    print("Jalan")
RedGreen()
Yellow()

if R1 === 0:
    print("stop)
RedGreen()
Yellow()

```

### Output program: 
    ```
    # jika lampu hijau nyala (lampu merah mati)
    if R1 == 1:
        print("Jalan")
        # Cacah mundur 60 detik.
        59
        58
        dst. 
    
        # setelah 60 detik...
        print("siap-siap...")
        3
        2
        1

        print("berhenti")
        # Cacah mundur 60 detik
        59
        58
        dst.

        # setelah 60 detik
        # setelah 60 detik...
        print("siap-siap...")
        3
        2
        1
     
     # jika lampu merah nyala (hijau mati)
     if R1 == 0:
        print("Berhenti")
        # Cacah mundur 60 detik.
        59
        58
        dst. 
    
        # se5telah 60 detik...
        print("siap-siap...")
        3
        2
        1

        print("Jalan")
        # Cacah mundur 60 detik
        59
        58
        dst.

        # setelah 60 detik
        # setelah 60 detik...
        print("siap-siap...")
        3
        2
        1
     
     else:
        print("masukkan input nyala lampu merah saja")
 
    ```
    - looping if else akan terus dilakukan



### Potongan program
```
Program Lampu Lalu Lintas 1 ruas jalan

import time

"""
on = 1
off = 0
"""
R1 = int(input("Nyala lampu merah: "))

while R1 >= 0:
    if R1 == 1:
        # Untuk lampu merah
        print("setop")
        3

            # Untuk lampu kuning
        for y in range(3, 0, -1):
            print(y)
            time.sleep(1)
        
        print("jalan")

            # Untuk lampu hijau
        for g in range(3,0,-1):
            print(g)
            time.sleep(1)
        
        break #klo ga ada ini jalan terus

    else: 
        print("jalan")

            # Untuk lampu hijau
        for g in range(5,0,-1):
            print(g)
            time.sleep(1)
        
        for y in range(3, 0, -1):
            print(y)
            time.sleep(1)
        

        print("setop cuy lagi merah")
        for r in range(5,0,-1):
            print(r)
            time.sleep(1)
        print("siap-siappp")
```
