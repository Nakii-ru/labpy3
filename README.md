# Praktikum 3 - Perulangan
RIDHO FHADLY HAMZAH

312410486

TI 24 A5

## Latihan 1
1. Tampilkan n bilangan acak yang lebih kecil dari 0.5.
2. nilai n diisi pada saat runtime
3. anda bisa menggunakan kombinasi while dan for untuk menyelesaikannya
4. gunakan fungsi random() yang dapat diimport terlebih dahulu

## Program Latihan 1
```python
from random import random

n = int(input("Masukkan nilai N: "))

for i in range(n):
    a = random()
    # Ulangi pengacakan jika nilai a >= 0.5
    while a >= 0.5:
        a = random()
    print(f"data ke: {i+1} => {a}")

print("Selesai")
```
## Penjelasan Kode
```python
from random import random
```
Mengimpor Fungsi random dari Modul Python bernama Random.
```python
n = int(input("Masukkan nilai N: "))
```
Meminta Input N dari Pengguna
```python
for i in range(n):
```
Melakukan Loop sesuai dengan nilai N yg diinputkan pengguna sebelumnya
```python
 a = random()
```
Variabel a diinisialisasi dengan nilai acak menggunakan random(), sehingga a memiliki nilai antara 0 dan 1.
```python
while a >= 0.5:
```
Jika nilai a yang dihasilkan lebih besar atau sama dengan 0.5, program akan mengulang proses pengacakan melalui while loop hingga menemukan nilai a yang kurang dari 0.5.
```python
 a = random()
```
Program mengacak kembali nilai a hingga menghasilkan nilai yang kurang dari 0.5. Setiap kali a >= 0.5, pernyataan a = random() dijalankan lagi, dan proses ini akan berulang hingga ditemukan nilai yang memenuhi syarat.
```python
print(f"data ke: {i+1} => {a}")
```
Bagian {i+1} digunakan untuk menampilkan nomor urutan data acak yang dihasilkan. Karena i dimulai dari 0, maka i+1 memberikan nomor urutan mulai dari 1 hingga N, sesuai input pengguna.
Bagian {a} akan mencetak nilai variabel a, yaitu nilai acak yang telah dihasilkan oleh random() dan memenuhi syarat a < 0.5.
Format String F-String
Dengan menggunakan f-string (f""), ekspresi atau variabel dapat langsung dimasukkan ke dalam string dalam {}.
Output akan menunjukkan nomor urut data serta nilai acak a yang dihasilkan.

## Hasil Eksekusi Latihan 1

## Latihan 2
Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal
awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga
baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%,
selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba
menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.

## Program Latihan 2
```python
modal_awal = 100_000_000

# Persentase laba bulanan
laba_per_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]

# Menghitung total keuntungan
total_keuntungan = 0

for i in range(8):
    keuntungan_bulan_ini = modal_awal * laba_per_bulan[i]
    total_keuntungan += keuntungan_bulan_ini
    print(f"Bulan {i+1}: Keuntungan = Rp {keuntungan_bulan_ini:,.2f}")

print(f"\nTotal keuntungan selama 8 bulan = Rp {total_keuntungan:,.2f}")
```
## Penjelasan Program
```python
modal_awal = 100_000_000
```
```python
laba_per_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]
```
```python
total_keuntungan = 0
```
```python
for i in range(8):
    keuntungan_bulan_ini = modal_awal * laba_per_bulan[i]
    total_keuntungan += keuntungan_bulan_ini
    print(f"Bulan {i+1}: Keuntungan = Rp {keuntungan_bulan_ini:,.2f}")
```
```python
print(f"\nTotal keuntungan selama 8 bulan = Rp {total_keuntungan:,.2f}")
```

## Hasil Eksekusi Latihan 2

## Latihan 3
Buat program yang mensimulasikan mesin ATM sederhana. Pengguna memiliki saldo awal
sebesar Rp 1.000.000, dan dapat menarik uang hingga saldo habis atau memilih untuk
keluar.

## Program Latihan 3
```python
saldo = 1000000
print("Selamat datang di mesin ATM sederhana!")
while True:
        print("1. Tarik Uang")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")
        
        if pilihan == '1':     
                jumlah = int(input("Masukkan jumlah uang yang ingin ditarik: Rp "))
                if jumlah > saldo:
                    print("Saldo tidak mencukupi.")
                elif jumlah <= 0:
                    print("Jumlah penarikan harus lebih dari nol.")
                else:
                    saldo -= jumlah
                    print(f"Anda berhasil menarik Rp {jumlah}. Saldo tersisa: Rp {saldo}")

        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM. Sampai jumpa!")
            break
```
## Penjelasan Program
```python
saldo = 1000000
```
```python
saldo = 1000000
print("Selamat datang di mesin ATM sederhana!")
```
```python
while True:
        print("1. Tarik Uang")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")
```
```python
 if pilihan == '1':     
                jumlah = int(input("Masukkan jumlah uang yang ingin ditarik: Rp "))
                if jumlah > saldo:
                    print("Saldo tidak mencukupi.")
```
```python
elif jumlah <= 0:
                    print("Jumlah penarikan harus lebih dari nol.")
```
```python
  else:
                    saldo -= jumlah
                    print(f"Anda berhasil menarik Rp {jumlah}. Saldo tersisa: Rp {saldo}")

```
```python
        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM. Sampai jumpa!")
            break
```
## Hasil Eksekusi Latihan 3
