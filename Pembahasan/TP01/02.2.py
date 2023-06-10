# Problem 2 : Pengelompokkan kelas berdasarkan NIM 

nim = int(input("Masukkan akhiran NIM :"))
kelompok = nim // 100

if nim % 100 == 0:
    kelompok -= 1

if kelompok > 2:
    kelompok = 3

if nim % 2 == 0:
    kelas = 2 * (kelompok+1)
else:
    kelas = 2 * kelompok + 1

print("Mahasiswa masuk ke kelas K" + str(kelas))