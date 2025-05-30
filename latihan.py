# praktek 1
"""

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# Input dari pengguna
try:
    angka = int(input("Masukkan angka untuk dihitung faktorialnya: "))
    if angka < 0:
        print("Faktorial tidak terdefinisi untuk angka negatif.")
    else:
        hasil = faktorial(angka)
        print(f"Faktorial dari {angka} adalah {hasil}")
except ValueError:
    print("Masukkan angka bulat yang valid.")

"""# praktek 2"""

# Inisialisasi list kosong
nilai_siswa = []

# Input nilai 5 siswa menggunakan loop
for i in range(5):
    while True:
        try:
            nilai = float(input(f"Masukkan nilai siswa ke-{i+1}: "))
            if 0 <= nilai <= 100:
                nilai_siswa.append(nilai)
                break
            else:
                print("Nilai harus antara 0 sampai 100.")
        except ValueError:
            print("Masukkan angka yang valid.")

# Mencari nilai tertinggi dan siswa keberapa yang mendapatkannya
nilai_tertinggi = max(nilai_siswa)
siswa_ke = nilai_siswa.index(nilai_tertinggi) + 1

# Menampilkan hasil
print("\n=== Hasil ===")
print(f"Nilai tertinggi adalah {nilai_tertinggi}")
print(f"Didapat oleh siswa ke-{siswa_ke}")
