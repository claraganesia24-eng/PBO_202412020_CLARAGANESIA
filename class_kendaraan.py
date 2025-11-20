class Kendaraan:
    # Class attribute
    bahan_bakar = "Bensin"

    # Constructor
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} warna {self.warna}, tahun {self.tahun}"
        

# Instansiasi objek
mobil1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
motor1 = Kendaraan("Honda Vario", "Merah", 2022)

# Demonstrasi akses instance attribute dan class attribute
print(mobil1.info_kendaraan())             # instance attribute
print(motor1.info_kendaraan())             # instance attribute

print(f"Bahan bakar mobil: {mobil1.bahan_bakar}")   # class attribute
print(f"Bahan bakar motor: {motor1.bahan_bakar}")   # class attribute

# Akses langsung ke class
print(f"Bahan bakar standar: {Kendaraan.bahan_bakar}")
