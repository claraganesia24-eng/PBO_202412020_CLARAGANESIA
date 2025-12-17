import tkinter as tk
from tkinter import ttk, messagebox, filedialog


# =========================
# CLASS MAHASISWA
# =========================
class Mahasiswa:
    def __init__(self, nim, nama, jurusan, ipk):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.ipk = ipk

    def info(self):
        return f"{self.nim} | {self.nama} | {self.jurusan} | {self.ipk}"

    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru


# =========================
# CLASS APLIKASI GUI
# =========================
class AplikasiMahasiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Mahasiswa")
        self.root.geometry("750x500")

        # Dictionary mahasiswa
        self.data_mahasiswa = {}

        self.buat_input()
        self.buat_tombol()
        self.buat_tabel()

    # =========================
    # INPUT DATA
    # =========================
    def buat_input(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="NIM").grid(row=0, column=0)
        tk.Label(frame, text="Nama").grid(row=1, column=0)
        tk.Label(frame, text="Jurusan").grid(row=2, column=0)
        tk.Label(frame, text="IPK").grid(row=3, column=0)

        self.entry_nim = tk.Entry(frame)
        self.entry_nama = tk.Entry(frame)
        self.entry_jurusan = tk.Entry(frame)
        self.entry_ipk = tk.Entry(frame)

        self.entry_nim.grid(row=0, column=1)
        self.entry_nama.grid(row=1, column=1)
        self.entry_jurusan.grid(row=2, column=1)
        self.entry_ipk.grid(row=3, column=1)

    # =========================
    # TOMBOL
    # =========================
    def buat_tombol(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Tambah", width=12, command=self.tambah).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Update IPK", width=12, command=self.update_ipk).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Hapus", width=12, command=self.hapus).grid(row=0, column=2, padx=5)
        tk.Button(frame, text="Cari", width=12, command=self.cari).grid(row=0, column=3, padx=5)

        tk.Button(frame, text="Rata-rata IPK", width=12, command=self.rata_ipk).grid(row=1, column=0, padx=5)
        tk.Button(frame, text="IPK Tertinggi", width=12, command=self.ipk_tertinggi).grid(row=1, column=1, padx=5)
        tk.Button(frame, text="Export TXT", width=12, command=self.export).grid(row=1, column=2, padx=5)

    # =========================
    # TABEL
    # =========================
    def buat_tabel(self):
        self.tree = ttk.Treeview(
            self.root,
            columns=("NIM", "Nama", "Jurusan", "IPK"),
            show="headings"
        )

        for col in ("NIM", "Nama", "Jurusan", "IPK"):
            self.tree.heading(col, text=col)

        self.tree.pack(fill=tk.BOTH, expand=True)

    def refresh(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for mhs in self.data_mahasiswa.values():
            self.tree.insert("", tk.END, values=(mhs.nim, mhs.nama, mhs.jurusan, mhs.ipk))

    # =========================
    # CRUD FUNCTION
    # =========================
    def tambah(self):
        nim = self.entry_nim.get()
        nama = self.entry_nama.get()
        jurusan = self.entry_jurusan.get()

        try:
            ipk = float(self.entry_ipk.get())
        except ValueError:
            messagebox.showwarning("Error", "IPK harus angka")
            return

        if not nim or not nama or not jurusan:
            messagebox.showwarning("Error", "Data tidak boleh kosong")
            return

        self.data_mahasiswa[nim] = Mahasiswa(nim, nama, jurusan, ipk)
        self.refresh()

    def update_ipk(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])['values'][0]
            try:
                ipk_baru = float(self.entry_ipk.get())
                self.data_mahasiswa[nim].update_ipk(ipk_baru)
                self.refresh()
            except ValueError:
                messagebox.showwarning("Error", "IPK tidak valid")

    def hapus(self):
        selected = self.tree.selection()
        if selected:
            nim = self.tree.item(selected[0])['values'][0]
            del self.data_mahasiswa[nim]
            self.refresh()

    def cari(self):
        keyword = self.entry_nim.get() or self.entry_nama.get()
        hasil = [
            m for m in self.data_mahasiswa.values()
            if keyword.lower() in m.nim.lower() or keyword.lower() in m.nama.lower()
        ]

        self.tree.delete(*self.tree.get_children())
        for m in hasil:
            self.tree.insert("", tk.END, values=(m.nim, m.nama, m.jurusan, m.ipk))

    # =========================
    # FITUR TAMBAHAN
    # =========================
    def rata_ipk(self):
        if not self.data_mahasiswa:
            return
        rata = sum(m.ipk for m in self.data_mahasiswa.values()) / len(self.data_mahasiswa)
        messagebox.showinfo("Rata-rata IPK", f"{rata:.2f}")

    def ipk_tertinggi(self):
        mhs = max(self.data_mahasiswa.values(), key=lambda m: m.ipk)
        messagebox.showinfo("IPK Tertinggi", mhs.info())

    def export(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt")
        if file:
            with open(file, "w") as f:
                for m in self.data_mahasiswa.values():
                    f.write(m.info() + "\n")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiMahasiswa(root)
    root.mainloop()
