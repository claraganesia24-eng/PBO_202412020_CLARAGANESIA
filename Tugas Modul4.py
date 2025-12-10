from abc import ABC, abstractmethod

# ==============================
# 1. Abstraction
# ==============================
class Pengguna(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def akses(self):
        pass


# ==============================
# 4. Custom Exception
# ==============================
class PoinTidakValidError(Exception):
    """Dilempar jika poin bernilai negatif."""
    pass


# ==============================
# 2. Special Methods + Turunan Class
# ==============================
class Member(Pengguna):
    def __init__(self, nama, poin):
        super().__init__(nama)
        self.poin = poin

    def akses(self):
        print(f"{self.nama} memiliki akses: Menggunakan layanan premium member.")

    def __str__(self):
        return f"Member: {self.nama} – Poin: {self.poin}"

    def __add__(self, other):
        return self.poin + other.poin

    def __len__(self):
        return len(self.nama)


# ==============================
# 3 & 5. Exception Handling + Program Utama
# ==============================
def input_poin():
    value = input("Masukkan poin: ")

    if value.strip() == "":
        raise ValueError("Input tidak boleh kosong!")

    if not value.isdigit():
        raise ValueError("Poin harus berupa angka!")

    poin = int(value)

    if poin < 0:
        raise PoinTidakValidError("Poin tidak boleh negatif!")

    return poin


if __name__ == "__main__":
    print("=== Membuat Member 1 ===")
    while True:
        try:
            p1 = input_poin()
            break
        except ValueError as e:
            print("Error:", e)
        except PoinTidakValidError as e:
            print("Error:", e)

    m1 = Member("Andi", p1)

    print("\n=== Membuat Member 2 ===")
    while True:
        try:
            p2 = input_poin()
            break
        except ValueError as e:
            print("Error:", e)
        except PoinTidakValidError as e:
            print("Error:", e)

    m2 = Member("Budi", p2)

    print("\n=== HASIL ===")
    print(m1)            # __str__
    print(m2)
    print("Total poin:", m1 + m2)   # __add__
    print("Panjang nama m1:", len(m1))  # __len__

    print("\nAkses Member:")
    m1.akses()
    m2.akses()
