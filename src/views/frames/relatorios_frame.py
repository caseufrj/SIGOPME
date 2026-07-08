import tkinter as tk


class RelatoriosFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = tk.Label(
            self,
            text="Relatórios",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)
