import tkinter as tk


class PacientesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        titulo = tk.Label(
            self,
            text="Pacientes",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=10)

        tk.Label(
            self,
            text="Cadastro de Pacientes"
        ).pack()
