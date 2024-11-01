from random import random

n = int(input("Masukkan nilai N: "))

for i in range(n):
    a = random()
    # Ulangi pengacakan jika nilai a >= 0.5
    while a >= 0.5:
        a = random()
    print(f"data ke: {i+1} => {a}")

print("Selesai")