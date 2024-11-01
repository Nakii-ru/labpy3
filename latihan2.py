# Modal awal
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