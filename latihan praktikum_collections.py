class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def info(self):
        return f"{self.judul} - {self.penulis} ({self.tahun})"


# List of objects
daftar_buku = [
    Buku("Python Dasar", "Hani", 2020),
    Buku("Pemrograman Java", "Melda", 2019),
    Buku("Basis Data", "Rapi", 2018),
    Buku("Algoritma", "Hanan", 2021),
    Buku("Aksara ku", "Clara", 2022)
]

# Fungsi pencarian berdasarkan penulis
def cari_buku(penulis):
    hasil = []
    for buku in daftar_buku:
        if buku.penulis.lower() == penulis.lower():
            hasil.append(buku)
    return hasil


# Eksekusi
penulis_cari = input("Masukkan nama penulis: ")
hasil = cari_buku(penulis_cari)

print("\n=== Hasil Pencarian ===")
if hasil:
    for buku in hasil:
        print(buku.info())
else:
    print("Buku tidak ditemukan.")
