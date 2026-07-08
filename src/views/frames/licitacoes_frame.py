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

        btn_novo = tk.Button(
            self,
            text="Novo"
        )

        btn_novo.pack(pady=5)

        btn_editar = tk.Button(
            self,
            text="Editar"
        )

        btn_editar.pack(pady=5)

        btn_excluir = tk.Button(
            self,
            text="Excluir"
        )

        btn_excluir.pack(pady=5)
