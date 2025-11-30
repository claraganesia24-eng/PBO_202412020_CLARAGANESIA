class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim                     # public
        self.nama = nama                   # public
        self._semester = semester          # protected
        self.__ipk = ipk                   # private

    # Getter semester
    def get_semester(self):
        return self._semester

    # Setter semester
    def set_semester(self, sem_baru):
        if sem_baru < 1:
            raise ValueError("Semester tidak boleh kurang dari 1.")
        self._semester = sem_baru

    # Getter IPK (private → wajib pakai getter)
    def get_ipk(self):
        return self.__ipk

    # Setter IPK (private → wajib pakai setter)
    def set_ipk(self, ipk_baru):
        if not (0 <= ipk_baru <= 4):
            raise ValueError("IPK harus antara 0 sampai 4.")
        self.__ipk = ipk_baru


# ================================
# Bagian Main Program
# ================================
if __name__ == "__main__":
    # Membuat objek
    m1 = Mahasiswa("23001", "Budi", 2, 3.2)
    m2 = Mahasiswa("23002", "Siti", 4, 3.8)

    print("=== Data Awal Mahasiswa ===")
    print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())

    # Mengganti semester dan IPK
    m1.set_semester(3)
    m1.set_ipk(3.6)

    m2.set_semester(5)
    m2.set_ipk(3.9)

    print("\n=== Data Setelah Diubah ===")
    print(m1.nim, m1.nama, m1.get_semester(), m1.get_ipk())
    print(m2.nim, m2.nama, m2.get_semester(), m2.get_ipk())
