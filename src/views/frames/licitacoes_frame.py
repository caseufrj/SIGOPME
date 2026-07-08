import tkinter as tk


class LicitacoesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = tk.Label(
            self,
            text="Licitações",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)
