class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        return f"Nama: {self.nama}, Umur: {self.umur}"


class Mahasiswa(Person):
    def __init__(self, nama, umur, nim):
        super().__init__(nama, umur)
        self.nim = nim

    def info(self):
        return f"Mahasiswa: {self.nama}, Umur: {self.umur}, NIM: {self.nim}"


# Instansiasi
p1 = Person("Clara", 19)
m1 = Mahasiswa("Melda", 20, "2305123456")

print(p1.info())
print(m1.info())
