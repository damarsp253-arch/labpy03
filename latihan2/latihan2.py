# latihan2.py
modal = 100000000
laba = 0

print("Modal awal:", modal)

for bulan in range(1, 9):
    if bulan in [1, 2]:
        persentase = 0
    elif bulan in [3, 4]:
        persentase = 0.01
    elif bulan in [5, 6, 7]:
        persentase = 0.05
    elif bulan == 8:
        persentase = 0.03
    
    keuntungan = modal * persentase
    laba += keuntungan
    print(f"Laba bulan ke-{bulan} sebesar: {keuntungan}")

print(f"Total laba adalah: {laba}")