import tkinter as tk

from views.frames.fornecedores_frame import FornecedoresFrame
from views.frames.pacientes_frame import PacientesFrame
from views.frames.usuarios_frame import UsuariosFrame


class CadastrosFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        titulo = tk.Label(
            self,
            text="Cadastros",
            font=("Arial", 18, "bold")
        )

        titulo.pack(pady=20)

        tk.Button(
            self,
            text="Fornecedores",
            width=25,
            command=self.abrir_fornecedores
        ).pack(pady=5)

        tk.Button(
            self,
            text="Pacientes",
            width=25,
            command=self.abrir_pacientes
        ).pack(pady=5)

        tk.Button(
            self,
            text="Usuários",
            width=25,
            command=self.abrir_usuarios
        ).pack(pady=5)

    def limpar_area(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

    def abrir_fornecedores(self):

        self.limpar_area()

        frame = FornecedoresFrame(self.parent)

        frame.pack(
            fill="both",
            expand=True
        )

    def abrir_pacientes(self):

        self.limpar_area()

        frame = PacientesFrame(self.parent)

        frame.pack(
            fill="both",
            expand=True
        )

    def abrir_usuarios(self):

        self.limpar_area()

        frame = UsuariosFrame(self.parent)

        frame.pack(
            fill="both",
            expand=True
        )
