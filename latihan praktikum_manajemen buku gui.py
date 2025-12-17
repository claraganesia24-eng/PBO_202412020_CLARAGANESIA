import tkinter as tk
from tkinter import ttk, messagebox


class Tugas:
    def __init__(self, nama, selesai=False):
        self.nama = nama
        self.selesai = selesai


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x350")

        # List of objects
        self.daftar_tugas = []

        # Entry input
        self.entry = tk.Entry(root, width=30)
        self.entry.pack(pady=5)

        # Tombol
        tk.Button(root, text="Tambah", command=self.tambah).pack(pady=2)
        tk.Button(root, text="Edit", command=self.edit).pack(pady=2)
        tk.Button(root, text="Hapus", command=self.hapus).pack(pady=2)
        tk.Button(root, text="Tandai Selesai", command=self.selesai).pack(pady=2)

        # Treeview
        self.tree = ttk.Treeview(
            root,
            columns=("Tugas", "Status"),
            show="headings"
        )
        self.tree.heading("Tugas", text="Tugas")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=5)

    def refresh(self):
        # Kosongkan tabel
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Tampilkan ulang data
        for tugas in self.daftar_tugas:
            status = "Selesai" if tugas.selesai else "Belum"
            self.tree.insert("", tk.END, values=(tugas.nama, status))

    def tambah(self):
        nama = self.entry.get()
        if nama:
            self.daftar_tugas.append(Tugas(nama))
            self.entry.delete(0, tk.END)
            self.refresh()
        else:
            messagebox.showwarning("Peringatan", "Masukkan nama tugas!")

    def edit(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            nama_baru = self.entry.get()

            if nama_baru:
                self.daftar_tugas[index].nama = nama_baru
                self.entry.delete(0, tk.END)
                self.refresh()
            else:
                messagebox.showwarning("Peringatan", "Masukkan nama tugas baru!")
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan diedit!")

    def hapus(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            del self.daftar_tugas[index]
            self.refresh()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas yang akan dihapus!")

    def selesai(self):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            self.daftar_tugas[index].selesai = True
            self.refresh()
        else:
            messagebox.showwarning("Peringatan", "Pilih tugas!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
