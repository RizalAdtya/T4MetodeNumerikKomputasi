import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

iterasi = 10
a = 9
b = 4
c = 3

hasil1 = np.zeros(iterasi, dtype=float)
hasil2 = np.zeros(iterasi, dtype=float)
x = np.zeros(iterasi, dtype=float)  # Variabel x untuk gx1
gx1 = np.zeros(iterasi, dtype=float)
epsT_1 = np.zeros(iterasi+1, dtype=float)
epsA_1 = np.zeros(iterasi+1, dtype=float)

# Menghitung akar-akar dari persamaan kuadratik
x[0] = 0  # Nilai awal yang dipilih secara arbitrer untuk gx1
x[1] = 1

for i in range(1, iterasi-1):  # Memulai iterasi dari 1
    denominator = 4*x[i] - 4
    if denominator != 0:  # Memastikan tidak ada pembagian dengan nol
        gx1[i] = x[i] - ((x[i]**4 - 4*x[i] - 9) / denominator)
        x[i+1] = gx1[i]  # Memperbaharui nilai x1 menggunakan gx1
        epsT_1[i] = abs((x[i+1] - x[i])) * 100
        epsA_1[i] = abs((gx1[i] - gx1[i-1]) / gx1[i]) * 100 if gx1[i] != 0 else 0
    else:
        gx1[i] = np.nan  # Menandai nilai yang tidak valid
        epsT_1[i] = np.nan
        epsA_1[i] = np.nan

# Buat daftar data untuk tabel
data = []
for i in range(1, iterasi):
    row = [i, gx1[i], epsT_1[i], epsA_1[i]]
    data.append(row)

# Buat header tabel
header = ["iterasi", "hasil 1", "epsT 1", "epsA 1"]

# Tampilkan tabel menggunakan tabulate
print(tabulate(data, headers=header))

# Plot
plt.plot(range(1, iterasi-1), gx1[1:iterasi-1], label='gx1: (x^4 - 9) / 2')
plt.xlabel('Iterasi')
plt.ylabel('Nilai')
plt.title('Perbandingan Hasil dari Iterasi')
plt.legend()
plt.grid(True)
plt.show()
