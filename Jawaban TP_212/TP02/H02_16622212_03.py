# NIM/Nama : 16622212/Siti Ramadina G.K.
# Tanggal : 06/10/2022
# Problem 3 : Faktor Prima Bilangan N

"""
Test Case 1 :
N = 110 
Faktor primanya adalah 2,5,11

Test Case 2 : 
N = 160
Faktor primanya adalah 2,5
"""

N = int(input("Masukkan N : "))

# Bilangan prima
bil_prima = [2,3,5,7,9,11,13,17,19,23,29,31,37]

# Faktor prima
print("Faktor primanya adalah : ", end="")
for i in bil_prima: #untuk i pada rentang dalam bilangan prima
    bagi = N % i
    if (bagi == 0):
        print(i,end=" ")
    


