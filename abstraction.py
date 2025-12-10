from abc import ABC, abstractmethod
import math

class Bentuk(ABC):

    @abstractmethod
    def luas(self):
        pass

    @abstractmethod
    def keliling(self):
        pass


class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        return math.pi * (self.jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.jari_jari


class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar, warna=None):
        self.panjang = panjang
        self.lebar = lebar
        self.warna = warna

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def info(self):
        print(f"Panjang: {self.panjang}")
        print(f"Lebar: {self.lebar}")
        if self.warna:
            print(f"Warna: {self.warna}")
