## Program Persimpangan Jalan (tanpa animasi)

```
# Gambar persimpangan
persimpangan = [
    "             J2  J1",
    "           | ^      |",
    "           | |    | |",
    "           |      v |",
    "           |        |",
    "   --------+     T1 +--------",
    "J3   -->  T2             --> J8",
    "J4  <--             T4  <--  J7",
    "   --------+ T3     +--------",
    "           |        |",
    "           | ^      |",
    "           | |    | |",
    "           |      v |",
    "             J5  J6",
]
print("Keterangan tabel: ")
print("b = langsung belok")
print("Tn = harus melalui lampu lalu lintas dulu (n = 1,2,3,4")
hubungan = [
    "   | J2 | J4 | J6 | J8 ",
    "---+----+----+----+----+----+----+----",
    "J1 |    | T1 | T1 | b  ",
    "J3 | b  |    | T2 | T2 ",
    "J5 | T3 | b  |    | T3 ",
    "J7 | T4 | T4 | b  |    ",
]

"""
untuk L genap (2,4,6,8) tidak ditulis karena tujuan jalan
"""
print("Keterangan: ")
print("hijau = 0")
print("kuning = 1")
print("merah = 2")

# Gantian berjalan (total 20s)
# Lampu 1 
T1 = [0,0,0,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
print("T1 = 3s hijau, 2s kuning, 15s merah")
# print("T1 =", T1)

# Lampu 2
T2 = [2,2,2,2,2,0,0,0,1,1,2,2,2,2,2,2,2,2,2,2]
print("T2 = 5s merah, 3s hijau, 2s kuning, 10s merah")
# print("T2 =", T2)

# Lampu 3
T3 = [2,2,2,2,2,2,2,2,2,2,0,0,0,1,1,2,2,2,2,2]
print("T3 = 10s merah, 3s hijau, 2s kuning, 5s merah")
# print("T3 =", T3)

# Lampu 4
T4 = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,1,1]
print("T4 = 15s merah, 3s hijau, 2s kuning")
# print("T4 =", T4)

import time

print("Persimpangan")
for i in persimpangan:
    print(i)
print()

print("Hubungan")
for i in hubungan:
    print(i)
print()

print("Traffic light")
print("  t  |   T1    |    T2   |    T3   |    T4   ")
print("-----+---------+---------+---------+---------")

N = len(T1)
t = 0

msg = [
    "  jalan  ", 
    "siap-siap", 
    " berhenti"
]
while(True):
    for i in range(N):
        time.sleep(0.5)

        print(f'{t:>4}', sep='', end=' |')
        print(msg[T1[i]], end='|')
        print(msg[T2[i]], end='|')
        print(msg[T3[i]], end='|')
        print(msg[T4[i]], end='')
        print(end='\r')
        
        t += 1
 ```
