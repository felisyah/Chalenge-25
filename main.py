import fisika
import time

import fisika.MassaJenis

def batas():
    print("-"*15)

waktu_awal = time.time()

print(f"Massa Jenis = {fisika.MassaJenis.MassaJenis(10,2)}")
print(f"Massa = {fisika.MassaJenis.Massa(10, 2)}")
print(f"Volume = {fisika.MassaJenis.Volume(10,2)}")
waktu_akhir = time.time()
print(f"Waktu yang dibutuhkan : {waktu_akhir - waktu_awal}")

batas()
print(f"Usaha = { fisika.U(12, 3)}")
print(f"Gaya = { fisika.G(6, 2)}")
print(f"Jarak = { fisika.J(9, 3)}")

batas()

print(f"Hasil Energi Potensial : {fisika.Ep(4, 7, 4) }")

batas()
print(f"Hasil Energi Kinetik : {fisika.Ek(4, 7) }")

batas()
diskon10 = fisika.Jl(10)
diskon20 = fisika.Jl(20)
diskon30 = fisika.Jl(30)
print(f"diskon 10% = diskon {diskon10(10000)}")
print(f"diskon 20% = diskon {diskon20(10000)}")
print(f"diskon 30% = diskon {diskon30(10000)}")