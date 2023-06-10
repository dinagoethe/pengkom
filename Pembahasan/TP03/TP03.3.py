
w1 = input("Masukkan string 1:")
l1 = len(w1)
print("Panjang string 1: ", l1)
w2 = input("Masukkan string 2:")
l2 = len(w2)
print("Panjang string 1: ", l2)

ans = 0
for i in range(l2-l1+1):
    sama = True
    for j in range(l1):
        if (w1[j] != w2[i+j]):
            sama = False
    
    if sama:
        ans += 1

print(f"String 1 muncul sebanyak {ans} kali")