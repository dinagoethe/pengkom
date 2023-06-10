# Pembahasan Tugas Pendahuluan
# Pembahasan Problem 2
# Problem 2 : Pengelompokkan kelas berdasarkan NIM 

# Alternatif 1
nim = int(input("Masukkan akhiran NIM : "))
if nim <= 100:
  if nim % 2 == 0:
    print("Mahasiswa masuk ke kelas K2")
  else:
    print("Mahasiswa masuk ke kelas K1")
elif nim <= 200:
  if nim % 2 == 0:
    print("Mahasiswa masuk ke kelas K4")
  else:
    print("Mahasiswa masuk ke kelas K3")
elif nim <= 300:
  if nim % 2 == 0:
    print("Mahasiswa masuk ke kelas K6")
  else:
    print("Mahasiswa masuk ke kelas K5")
elif nim <= 400:
  if nim % 2 == 0:
    print("Mahasiswa masuk ke kelas K8")
  else:
    print("Mahasiswa masuk ke kelas K7")

# Alternatif 2 (versi pendek)
kelas = ""
nim = int(input("Masukkan akhiran NIM : "))
if nim <= 100:
  if nim % 2 == 0:
    kelas = "K2"
  else:
    kelas = "K1"
if nim <= 200:
  if nim % 2 == 0:
    kelas = "K4"
  else:
    kelas = "K3"
if nim <= 300:
  if nim % 2 == 0:
    kelas = "K6"
  else:
    kelas = "K5"
else:
  if nim % 2 == 0:
    kelas = "K8"
  else:
    kelas = "K7"

print("Mahasiswa masuk ke kelas", kelas)


