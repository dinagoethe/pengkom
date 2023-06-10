N = int(input("Masukkan banyak lampu: "))
jumlah = int(input("Masukkan berapa kali Tuan Kil menekan tombol: "))

lamp = [0 for i in range(N)]
for i in range(jumlah):
    perintah = int(input(f"Tombol yang ditekan ke-{i+1}: "))
    # Mengubah tombol pertama dan sebelahnya
    if (perintah == 1):
        for j in range(perintah-1,perintah+1):
            if lamp[j] == 0:
                lamp[j] = 1
            else:
                lamp[j] = 0
    elif (perintah == N):
        # Mengubah tombol terakhir dan sebelumnya
        for j in range(perintah-2,perintah):
            if lamp[j] == 0:
                lamp[j] = 1
            else:
                lamp[j] = 0
    else:
        for j in range(perintah-2, perintah+1):
            if lamp[j] == 0:
                lamp[j] = 1
            else:
                lamp[j] = 0

print("Keadaan akhir lampu adalah", end="")
for i in range(N):
    print(lamp[i], end="")
