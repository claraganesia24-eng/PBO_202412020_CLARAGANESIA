import tkinter as tk
from tkinter import messagebox


class AplikasiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Sederhana")
        self.root.geometry("300x200")

        tk.Label(root, text="Masukkan Nama").pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        tk.Button(root, text="Tampilkan", command=self.tampilkan).pack(pady=5)
        tk.Button(root, text="Hapus", command=self.hapus).pack(pady=5)

    def tampilkan(self):
        nama = self.entry.get()
        if nama:
            messagebox.showinfo("Info", f"Halo {nama}")
        else:
            messagebox.showwarning("Warning", "Nama kosong!")

    def hapus(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiGUI(root)
    root.mainloop()
