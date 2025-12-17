import tkinter as tk


class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Sederhana")
        self.root.geometry("300x400")

        # Variabel untuk menyimpan ekspresi
        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 18),
            bd=10,
            relief=tk.RIDGE,
            justify=tk.RIGHT
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Tombol
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                tk.Button(
                    root, text=button, width=8, height=2,
                    command=self.hitung
                ).grid(row=row_val, column=col_val, padx=5, pady=5)

            elif button == 'C':
                tk.Button(
                    root, text=button, width=8, height=2,
                    command=self.hapus
                ).grid(row=row_val, column=0, columnspan=4, sticky="we", padx=5, pady=5)
                row_val += 1
                col_val = 0
                continue
