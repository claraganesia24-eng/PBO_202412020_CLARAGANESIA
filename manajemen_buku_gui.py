import tkinter as tk
from tkinter import messagebox, ttk, simpledialog


class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun


class AplikasiManajemenBuku:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Buku")
        self.root.geometry("600x400")

        self.daftar_buku = []

        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack()

        tk.Label(frame_input, text="Judul").grid(row=0, column=0)
        self.entry_judul = tk.Entry(frame_input, width=30)
        self.entry_judul.grid(row=0, column=1)

        tk.Label(frame_input, text="Penulis").grid(row=1, column=0)
        self.entry_penulis = tk.Entry(frame_input, width=30)
        self.entry_penulis.grid(row=1, column=1)

        tk.Label(frame_input, text="Tahun").grid(row=2, column=0)
        self.entry_tahun = tk.Entry(frame_input, width=30)
        self.entry_tahun.grid(row=2, column=1)

        frame_tombol = tk.Frame(root)
        frame_tombol.pack()

        tk.Button(frame_tombol, text="Tambah", command=self.tambah_buku).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Hapus", command=self.hapus_buku).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_tombol, text="Cari", command=self.cari_buku).pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(root, columns=("Judul", "Penulis", "Tahun"), show="headings")
        self.tree.heading("Judul", text="Judul")
        self.tree.heading("Penulis", text="Penulis")
        self.tree.heading("Tahun", text="Tahun")
        self.tree.pack(fill=tk.BOTH, expand=True)

    def tambah_buku(self):
        judul = self.entry_judul.get()
        penulis = self.entry_penulis.get()
        tahun = self.entry_tahun.get()

        if judul and penulis and tahun:
            buku = Buku(judul, penulis, tahun)
            self.daftar_buku.append(buku)
            self.tree.insert("", tk.END, values=(judul, penulis, tahun))

            self.entry_judul.delete(0, tk.END)
            self.entry_penulis.delete(0, tk.END)
            self.entry_tahun.delete(0, tk.END)
        else:
            messagebox.showwarning("Peringatan", "Semua field harus diisi!")

    def hapus_buku(self):
        selected = self.tree.selection()
        if selected:
            self.tree.delete(selected[0])
        else:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu!")

    def cari_buku(self):
        keyword = simpledialog.askstring("Cari", "Masukkan judul / penulis:")
        if keyword:
            hasil = [
                b for b in self.daftar_buku
                if keyword.lower() in b.judul.lower()
                or keyword.lower() in b.penulis.lower()
            ]

            if hasil:
                pesan = ""
                for b in hasil:
                    pesan += f"{b.judul} - {b.penulis} ({b.tahun})\n"
                messagebox.showinfo("Hasil", pesan)
            else:
                messagebox.showinfo("Hasil", "Buku tidak ditemukan")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiManajemenBuku(root)
    root.mainloop()
