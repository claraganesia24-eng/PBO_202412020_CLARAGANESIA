import tkinter as tk
from tkinter import messagebox


class KonversiSuhu:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Suhu")
        self.root.geometry("250x200")

        tk.Label(root, text="Celsius").pack(pady=5)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        tk.Button(root, text="Konversi", command=self.konversi).pack(pady=5)
        tk.Button(root, text="Hapus", command=self.hapus).pack(pady=5)

    def konversi(self):
        try:
            c = float(self.entry.get())
            f = (c * 9 / 5) + 32
            messagebox.showinfo("Hasil", f"{f} Fahrenheit")
        except ValueError:
            messagebox.showwarning("Error", "Input harus berupa angka!")

    def hapus(self):
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = KonversiSuhu(root)
    root.mainloop()
