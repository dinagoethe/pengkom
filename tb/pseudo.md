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
        for r in range(3,0,-1):
            print(r)
            time.sleep(1)
        print("siap-siappp")

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
