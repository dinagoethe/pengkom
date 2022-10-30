```
Program Lampu Lalu Lintas akan ditulis di sini

import time

"""
on = 1
off = 0
"""
N = 3
R1 = int(input("Nyala lampu merah: "))


while R1 >= 0:
    if R1 == 1:
        # Untuk lampu merah
        print("setop cuy lagi merah")
        for r in range(3,0,-1):
            print(r)
            time.sleep(1)
        print("siap-siappp")

            # Untuk lampu kuning
        for y in range(3, 0, -1):
            print(y)
            time.sleep(1)
        
        print("jalan woi dah ijo!")

            # Untuk lampu hijau
        for g in range(3,0,-1):
            print(g)
            time.sleep(1)
        
        break

    else: 
        print("jalan woi dah ijo!")

            # Untuk lampu hijau
        for g in range(5,0,-1):
            print(g)
            time.sleep(1)
        
        for y in range(3, 0, -1):
            print(y)
            time.sleep(1)
        
        print("jalan woi dah ijo!")

        print("setop cuy lagi merah")
        for r in range(5,0,-1):
            print(r)
            time.sleep(1)
        print("siap-siappp")
```
