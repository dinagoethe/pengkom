Program jadi yang memuat:
1. Array dan fungsi pencacahan waktu (*countdown*)
2. If conditional
3. Pemanggilan fungsi subprogram
4. Perulangan (*while loop*)

*Minus matrix

```
import time

N = 60
T = [i for i in range(N, 0, -1)]

n = 3
t = [i for i in range(n, 0, -1)]

def lampu(L):
    for i in T: 
            print(i)
            time.sleep(1)

def siapHijau(L):
    print("Siap-siap lampu hijau..")
    for i in t:
        print(i)
        time.sleep(1)

def siapMerah(L):
    print("Bentar lagi lampu merah...!")
    for i in t:
        print(i)
        time.sleep(1)

print("Kondisi lampu:")
print("ON = 1")
print("OFF = 0")
G1 = int(input("Kondisi lampu hijau? "))

while G1 >= 0:
    if G1 == 1:
        print("Jalan!")
        lampu(G1)
        siapMerah(G1)
        print("Berhenti!")
        lampu(G1)
        siapHijau(G1)

    if G1 == 0:
        print("Berhenti")
        lampu(G1)
        siapHijau(G1)
        print("Jalan!")
        lampu(G1)
        siapMerah(G1)
```
