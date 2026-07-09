import tkinter as tk
from views.components.grid_helper import criar_treeview


class MovimentacoesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = tk.Label(
            self,
            text="Movimentações",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)
