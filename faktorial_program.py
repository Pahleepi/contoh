def faktorial(n):
    """
    Fungsi rekursif untuk menghitung faktorial dari sebuah angka.
    
    Args:
        n (int): Angka yang akan dihitung faktorialnya
        
    Returns:
        int: Hasil faktorial dari angka n
    """
    # Kasus dasar: faktorial dari 0 dan 1 adalah 1
    if n == 0 or n == 1:
        return 1
    # Kasus rekursif: n! = n * (n-1)!
    else:
        return n * faktorial(n-1)

def main():
    try:
        # Meminta input dari pengguna
        angka = int(input("Masukkan angka untuk dihitung faktorialnya: "))
        
        # Validasi input
        if angka < 0:
            print("Faktorial tidak dapat dihitung untuk angka negatif.")
        else:
            # Hitung dan tampilkan hasilnya
            hasil = faktorial(angka)
            print(f"Faktorial dari {angka} adalah {hasil}")
    except ValueError:
        print("Input tidak valid. Mohon masukkan bilangan bulat positif.")
    except RecursionError:
        print("Angka terlalu besar untuk dihitung faktorialnya dengan rekursi.")

# Menjalankan program
if __name__ == "__main__":
    main()
