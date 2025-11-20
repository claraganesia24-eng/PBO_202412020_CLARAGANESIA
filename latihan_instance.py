class ManajerInventori:
    def __init__(self):
        # inventori disimpan sebagai dictionary: {nama_barang: jumlah}
        self.inventori = {}

    def tambah_barang(self, nama, jumlah):
        if jumlah > 0:
            if nama in self.inventori:
                self.inventori[nama] += jumlah
            else:
                self.inventori[nama] = jumlah
            return f"Berhasil menambah {jumlah} {nama}. Total: {self.inventori[nama]}"
        return "Jumlah harus positif"

    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return f"{nama} tidak ditemukan di inventori"

        if 0 < jumlah <= self.inventori[nama]:
            self.inventori[nama] -= jumlah

            if self.inventori[nama] == 0:
                del self.inventori[nama]  # hapus barang jika stok habis

            return f"Berhasil mengurangi {jumlah} {nama}"
        return "Jumlah tidak valid atau melebihi stok"

    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        return f"Daftar inventori: {self.inventori}"


# Demonstrasi method
manager = ManajerInventori()

print(manager.tambah_barang("Pensil", 50))
print(manager.tambah_barang("Buku", 20))
print(manager.tambah_barang("Pensil", 10))

print(manager.hapus_barang("Buku", 5))
print(manager.hapus_barang("Pensil", 60))   # contoh gagal
print(manager.hapus_barang("Pensil", 40))

print(manager.lihat_inventori())
