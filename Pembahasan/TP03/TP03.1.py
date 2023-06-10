N = int(input("Masukkan banyak barang: "))

# Inisialisassi array harga dan diskon
harga = [0 for i in range(N)]
diskon = [0 for i in range(N)]

# Mengisi array
for i in range(N):
    harga[i] = int(input(f"Masukkan harga awal barang ke-{i+1}: "))

for i in range(N):
    diskon[i] = int(input(f"Masukkan diskon (dalam persen) barang ke-{i+1}: "))

print(harga)
print(diskon)
# Mencari nilai maks
idx = 0
max = 0
for i in range(N):
    x = harga[i]*diskon[i]
    print(x)
    if x > max:
        max = x
        idx = i + 1

print(f"Barang {idx} memiliki diskon paling besar yaitu {max}")