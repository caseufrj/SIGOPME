import tkinter as tk
from tkinter import messagebox

from services.paciente_service import PacienteService

from views.components.grid_helper import criar_treeview
from views.components.search_helper import criar_barra_pesquisa

class PacientesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()
        self.carregar_dados()

    def criar_componentes(self):

        titulo = tk.Label(
            self,
            text="Pacientes",
            font=("Arial", 18, "bold")
        )
    
        titulo.pack(
            pady=10
        )
    
        barra = tk.Frame(self)
    
        barra.pack(
            fill="x",
            padx=10,
            pady=5
        )
    
        tk.Button(
            barra,
            text="Novo",
            command=self.novo
        ).pack(
            side="left",
            padx=5
        )
    
        tk.Button(
            barra,
            text="Editar",
            command=self.editar
        ).pack(
            side="left",
            padx=5
        )
    
        tk.Button(
            barra,
            text="Excluir",
            command=self.excluir
        ).pack(
            side="left",
            padx=5
        )
    
        frame_pesquisa, self.txt_pesquisa = criar_barra_pesquisa(
            barra
        )
    
        frame_pesquisa.pack(
            side="right"
        )
    
        colunas = (
            "id",
            "registro",
            "nome",
            "nascimento"
        )
    
        frame_grid, self.grid = criar_treeview(
            self,
            colunas
        )
    
        frame_grid.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.grid.heading(
            "id",
            text="Id"
        )
    
        self.grid.heading(
            "registro",
            text="Registro"
        )
    
        self.grid.heading(
            "nome",
            text="Nome"
        )
    
        self.grid.heading(
            "nascimento",
            text="Data Nascimento"
        )

        self.grid.column(
            "id",
            width=0,
            stretch=False
        )
    
        self.grid.column(
            "registro",
            width=120
        )
    
        self.grid.column(
            "nome",
            width=350
        )
    
        self.grid.column(
            "nascimento",
            width=130
        )

        self.lbl_total = tk.Label(
            self,
            text="0 registros"
        )
    
        self.lbl_total.pack(
            pady=5
        )

    def carregar_dados(self):

        for item in self.grid.get_children():
            self.grid.delete(item)
    
        dados = PacienteService.listar_todos()
    
        for paciente in dados:
    
            self.grid.insert(
                "",
                "end",
                values=paciente
            )
    
        self.lbl_total.config(
            text=f"{len(dados)} registros"
        )

    def novo(self):

        messagebox.showinfo(
            "SIGOPME",
            "Novo paciente."
        )
    
    
    def editar(self):
    
        messagebox.showinfo(
            "SIGOPME",
            "Editar paciente."
        )
    
    
    def excluir(self):
    
        messagebox.showinfo(
            "SIGOPME",
            "Excluir paciente."
        )
