import tkinter as tk


class UsuariosFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = tk.Label(
            self,
            text="Usuários",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=10)

        tk.Label(
            self,
            text="Cadastro de Usuários"
        ).pack()
