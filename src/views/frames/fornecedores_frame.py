import tkinter as tk
from tkinter import ttk


class FornecedoresFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = tk.Label(
            self,
            text="Fornecedores",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )
