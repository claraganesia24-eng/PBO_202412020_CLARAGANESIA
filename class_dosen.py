class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    def ajar_mata_kuliah(self, mata_kuliah):
        return f"Dosen {self.nama} (NIDN: {self.nidn}) mengajar mata kuliah {mata_kuliah}"


# Instansiasi objek dosen
dosen1 = Dosen("Dr. fardy", "123456")
dosen2 = Dosen("Prof. Ratma", "654321")

# Pemanggilan method
print(dosen1.ajar_mata_kuliah("Algoritma dan Pemrograman"))
print(dosen2.ajar_mata_kuliah("Basis Data"))
