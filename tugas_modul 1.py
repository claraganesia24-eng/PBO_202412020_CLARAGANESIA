class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan
    def perkenalan_diri(self):
        return (f"Halo, saya {self.nama} (NIM: {self.nim}) dari jurusan {self.jurusan} "
                f"mahasiswa {Mahasiswa.universitas} dengan IPK {self.ipk}")

    # Method update IPK
    def update_ipk(self, ipk_baru):
        if 0.0 <= ipk_baru <= 4.0:
            self.ipk = ipk_baru
            return f"IPK berhasil diperbarui menjadi {self.ipk}"
        return "IPK tidak valid"

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Tidak Lulus"


# ---------------------------
# Instansiasi 3 objek mahasiswa
# ---------------------------

m1 = Mahasiswa("Clara Ganesia", "TI020", "Teknik Informatika", 3.7)
m2 = Mahasiswa("Alan Walker", "TI002", "Teknik Informatika", 3.4)
m3 = Mahasiswa("Rina Rini", "SI003", "Sistem Informasi", 2.6)

# Demonstrasi method
print(m1.perkenalan_diri())
print(m1.predikat_kelulusan())
print()

print(m2.perkenalan_diri())
print(m2.predikat_kelulusan())
print()

print(m3.perkenalan_diri())     # sebelum update IPK
print(m3.predikat_kelulusan())

print(m3.update_ipk(2.8))       # update IPK
print(m3.predikat_kelulusan())  # setelah update
