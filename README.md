# Praktikum 3 - Perulangan
NAMA    : RIDHO FHADLY HAMZAH

NIM     : 312410486

KELAS   : TI.24.A.5

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
Meminta Input `N` dari Pengguna
```python
for i in range(n):
```
Melakukan Loop sesuai dengan nilai `N` yg diinputkan pengguna sebelumnya
```python
 a = random()
```
Variabel `a` diinisialisasi dengan nilai acak menggunakan `random()`, sehingga a memiliki nilai antara 0 dan 1.
```python
while a >= 0.5:
```
Jika nilai `a` yang dihasilkan lebih besar atau sama dengan `0.5`, program akan mengulang proses pengacakan melalui `while loop` hingga menemukan nilai `a` yang kurang dari `0.5`.
```python
 a = random()
```
Program mengacak kembali nilai `a` hingga menghasilkan nilai yang kurang dari `0.5`. Setiap kali `a` >= `0.5`, pernyataan `a` = `random()` dijalankan lagi, dan proses ini akan berulang hingga ditemukan nilai yang memenuhi syarat.
```python
print(f"data ke: {i+1} => {a}")
```
Bagian `{i+1}` digunakan untuk menampilkan nomor urutan data acak yang dihasilkan. Maka i+1 memberikan nomor urutan mulai dari 1 hingga N, sesuai input pengguna.

Bagian `{a}` akan mencetak nilai variabel a, yaitu nilai acak yang telah dihasilkan oleh random() dan memenuhi syarat a < 0.5.

Output akan menunjukkan nomor urut data serta nilai acak `a` yang dihasilkan.

## Hasil Eksekusi Latihan 1
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-11-01%20193310.png?raw=true)

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
Inisialisasi variabel modal_awal dengan nilai 100_000_000.
```python
laba_per_bulan = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]
```
`laba_per_bulan` berisi daftar persentase laba untuk setiap bulan selama 8 bulan.
```python
total_keuntungan = 0
```
Variabel `total_keuntungan` berfungsi untuk menyimpan total keuntungan yg akan terus diperbarui di setiap bulan selama iterasi.
```python
for i in range(8):
    keuntungan_bulan_ini = modal_awal * laba_per_bulan[i]
    total_keuntungan += keuntungan_bulan_ini
    print(f"Bulan {i+1}: Keuntungan = Rp {keuntungan_bulan_ini:,.2f}")
```
`for i in range(8)`: Loop ini akan berjalan sebanyak `8` kali, yaitu untuk 8 bulan.

menginisialisasi variabel `keuntungan_bulan_ini` = `modal_awal` * `laba_per_bulan[i]` 

`print(f"Bulan {i+1}: Keuntungan = Rp {keuntungan_bulan_ini:,.2f}")` untu menampilkan keuntungan yang didapatkan setiap bulan.

```python
print(f"\nTotal keuntungan selama 8 bulan = Rp {total_keuntungan:,.2f}")
```
Setelah loop selesai, total keuntungan yg sudah dihitung selama 8 bulan akan ditampilkan.

## Hasil Eksekusi Latihan 2
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-11-01%20193329.png?raw=true)

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
print("Selamat datang di mesin ATM sederhana!")
```
Program dimulai dengan inisialisasi saldo menjadi 1000000
```python
while True:
        print("1. Tarik Uang")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")
```
Saat program masuk ke dalam loop, menu atm akan terus memberikan 2 opsi kepada pengguna.
```python
 if pilihan == '1':     
                jumlah = int(input("Masukkan jumlah uang yang ingin ditarik: Rp "))
```
Jika pengguna memilih 1, program meminta jumlah uang yang ingin ditarik.
```python
                if jumlah > saldo:
                    print("Saldo tidak mencukupi.")
elif jumlah <= 0:
                    print("Jumlah penarikan harus lebih dari nol.")
  else:
                    saldo -= jumlah
                    print(f"Anda berhasil menarik Rp {jumlah}. Saldo tersisa: Rp {saldo}")

```
Program kemudian memeriksa beberapa kondisi:

`Saldo Tidak Mencukupi`: Jika jumlah yang dimasukkan lebih besar dari saldo, program menampilkan pesan bahwa saldo tidak mencukupi.

`Jumlah Penarikan Tidak Valid`: Jika jumlah yang dimasukkan kurang dari atau sama dengan nol

`Penarikan Berhasil`: Jika jumlah penarikan valid dan cukup, program mengurangi saldo dengan jumlah tersebut dan menampilkan saldo yang tersisa.

```python
        elif pilihan == '2':
            print("Terima kasih telah menggunakan ATM. Sampai jumpa!")
            break
```
Jika pengguna memilih `2`, program menampilkan pesan terima kasih dan keluar dari loop menggunakan `break`.

## Hasil Eksekusi Latihan 3
![foto](https://github.com/Nakii-ru/foto/blob/main/Screenshot%202024-11-01%20193947.png?raw=true)
