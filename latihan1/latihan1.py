# latihan1.py
from random import random

# input jumlah data
n = int(input("Masukkan nilai n: "))

i = 1
while i <= n:
    a = random()  # menghasilkan bilangan acak antara 0.0 - 1.0
    if a < 0.5:
        print("data ke-", i, "=>", a)
        i += 1  # hanya tambahkan jika < 0.5
    else:
        continue  # kalau >= 0.5, ulang lagi sampai dapat yang < 0.5

print("Selesai")