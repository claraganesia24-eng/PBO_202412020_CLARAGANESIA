class Bentuk:
    def luas(self):
        return 0


class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


class Lingkaran(Bentuk):
    def __init__(self, r):
        self.jari = r

    def luas(self):
        return 3.14 * self.jari * self.jari


# Demonstrasi
b = Bentuk()
p = Persegi(5)
l = Lingkaran(7)

print("Luas Bentuk:", b.luas())
print("Luas Persegi:", p.luas())
print("Luas Lingkaran:", l.luas())
