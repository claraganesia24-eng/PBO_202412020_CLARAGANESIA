# ==========================================
# CLASS BUKU
# ==========================================
class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        self.judul = judul               # public
        self.penulis = penulis           # public
        self.kode_buku = kode_buku       # public
        self._stok = stok                # protected
        self.__lokasi_rak = lokasi_rak   # private

    # Getter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    # Setter lokasi rak
    def set_lokasi_rak(self, lokasi):
        self.__lokasi_rak = lokasi

    # Tambah stok buku
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    # Kurangi stok buku
    def kurangi_stok(self, jumlah):
        if jumlah > self._stok:
            raise ValueError("Stok tidak mencukupi.")
        self._stok -= jumlah


# ==========================================
# CLASS PEMINJAMAN
# ==========================================
class Peminjaman:
    def __init__(self, kode_buku, tanggal_pinjam, tanggal_kembali, status):
        self.kode_buku = kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = status

    def info_peminjaman(self):
        return f"Buku {self.kode_buku} | Pinjam: {self.tanggal_pinjam} | Kembali: {self.tanggal_kembali} | Status: {self.status}"


# ==========================================
# CLASS ANGGOTA
# ==========================================
class Anggota:
    def __init__(self, id_anggota, nama, maks_pinjam, status_aktif=True):
        self.id_anggota = id_anggota              # public
        self.nama = nama                          # public
        self._maks_pinjam = maks_pinjam           # protected
        self.__status_aktif = status_aktif        # private
        self.daftar_peminjaman = []               # aggregation

    # Getter status aktif
    def get_status(self):
        return self.__status_aktif

    # Setter status aktif
    def set_status(self, status):
        self.__status_aktif = status

    # Pinjam buku
    def pinjam_buku(self, peminjaman: Peminjaman):
        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            raise ValueError("Sudah mencapai batas maksimum peminjaman.")
        self.daftar_peminjaman.append(peminjaman)

    # Kembalikan buku
    def kembalikan_buku(self, kode_buku):
        for p in self.daftar_peminjaman:
            if p.kode_buku == kode_buku:
                p.status = "Dikembalikan"
                return
        raise ValueError("Buku tidak ditemukan dalam daftar peminjaman.")


# ==========================================
# CLASS PERPUSTAKAAN (Composition)
# ==========================================
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.buku_list = []  # composition

    def tambah_buku(self, buku: Buku):
        self.buku_list.append(buku)


# ==========================================
# INSTANSIASI (Sesuai Instruksi)
# ==========================================
if __name__ == "__main__":
    perpustakaan = Perpustakaan("Perpustakaan Kota")

    # 3 buku
    b1 = Buku("Pemrograman Python", "Wahyu", "B001", 3, "Rak A1")
    b2 = Buku("Basis Data", "Lina", "B002", 2, "Rak B3")
    b3 = Buku("Jaringan Komputer", "Agus", "B003", 4, "Rak C2")

    perpustakaan.tambah_buku(b1)
    perpustakaan.tambah_buku(b2)
    perpustakaan.tambah_buku(b3)

    # 2 anggota
    a1 = Anggota("A001", "Budi", 2)
    a2 = Anggota("A002", "Siti", 2)

    # Anggota 1 pinjam 2 buku
    a1.pinjam_buku(Peminjaman("B001", "2025-01-01", "2025-01-07", "Dipinjam"))
    a1.pinjam_buku(Peminjaman("B002", "2025-01-02", "2025-01-08", "Dipinjam"))

    # Anggota 2 pinjam 1 buku
    a2.pinjam_buku(Peminjaman("B003", "2025-01-03", "2025-01-09", "Dipinjam"))

    # Pengembalian buku
    a1.kembalikan_buku("B002")

    # ================================
    # DEMONSTRASI OUTPUT
    # ================================
    print("\n=== Informasi Buku ===")
    for b in perpustakaan.buku_list:
        print(f"{b.kode_buku} - {b.judul} | Stok: {b._stok} | Rak: {b.get_lokasi_rak()}")

    print("\n=== Informasi Anggota ===")
    print(a1.id_anggota, "-", a1.nama, "| Status:", a1.get_status())
    print(a2.id_anggota, "-", a2.nama, "| Status:", a2.get_status())

    print("\n=== Daftar Peminjaman Anggota ===")
    print("Peminjaman", a1.nama)
    for p in a1.daftar_peminjaman:
        print(p.info_peminjaman())

    print("\nPeminjaman", a2.nama)
    for p in a2.daftar_peminjaman:
        print(p.info_peminjaman())
