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