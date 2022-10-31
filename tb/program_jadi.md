Program jadi yang memuat:
1. Array dan fungsi pencacahan waktu (*countdown*)
2. If conditional
3. Pemanggilan fungsi subprogram
4. Perulangan (*while loop*)

*Minus matrix

```
import time

N = 3
T = [i for i in range(N, 0, -1)]

n = 3
t = [i for i in range(n, 0, -1)]

def lampu(L):
    if L == 1:
        print("Jalan!")
    elif L == 0:
        print("Berhenti")

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

while G1>= 0:
    if G1 == 1:
        lampu(G1)
        for i in T: 
            print(i)
            time.sleep(1)
        
        
        print("Berhenti!")
        for i in T: 
            print(i)
            time.sleep(1)

        
    if G1 == 0:
        lampu(G1)
        for i in T: 
            print(i)
            time.sleep(1)
        
        siapHijau(G1)

        print("Jalan!")
        for i in T: 
            print(i)
            time.sleep(1)
        
        siapMerah(G1)
```
