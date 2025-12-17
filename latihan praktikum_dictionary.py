class Pelanggan:
    def __init__(self, id_pelanggan, nama, email):
        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.email = email

    def info(self):
        return f"{self.nama} - {self.email}"


data_pelanggan = {}


def tambah_pelanggan(pelanggan):
    data_pelanggan[pelanggan.id_pelanggan] = pelanggan


def hapus_pelanggan(id_pelanggan):
    if id_pelanggan in data_pelanggan:
        del data_pelanggan[id_pelanggan]


def cari_pelanggan(id_pelanggan):
    return data_pelanggan.get(id_pelanggan)


# Eksekusi
tambah_pelanggan(Pelanggan("PL001", "hani", "hani@email.com"))
tambah_pelanggan(Pelanggan("PL002", "Mas Al", "AL@email.com"))

print("=== Daftar Pelanggan ===")
for p in data_pelanggan.values():
    print(p.info())

print("\nCari PL002:")
pelanggan = cari_pelanggan("PL002")
if pelanggan:
    print(pelanggan.info())
