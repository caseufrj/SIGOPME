import tkinter as tk


class CadastrosFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = tk.Label(
            self,
            text="Cadastros",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=20
        )

        tk.Button(
            self,
            text="Fornecedores",
            width=25
        ).pack(
            pady=5
        )

        tk.Button(
            self,
            text="Pacientes",
            width=25
        ).pack(
            pady=5
        )

        tk.Button(
            self,
            text="Usuários",
            width=25
        ).pack(
            pady=5
        )
