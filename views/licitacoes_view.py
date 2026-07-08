import tkinter as tk
from tkinter import ttk


class LicitacoesView(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Licitações")
        self.geometry("1200x700")

        self.criar_componentes()

    def criar_componentes(self):

        frm_filtro = tk.Frame(self)
        frm_filtro.pack(fill="x", padx=10, pady=10)

        tk.Label(frm_filtro, text="Pesquisar").pack(side="left")

        self.txt_pesquisa = tk.Entry(frm_filtro, width=50)
        self.txt_pesquisa.pack(side="left", padx=10)

        btn_pesquisar = tk.Button(
            frm_filtro,
            text="Pesquisar"
        )

        btn_pesquisar.pack(side="left")

        colunas = (
            "Codigo",
            "Descricao",
            "Fornecedor",
            "Ata",
            "Qtd"
        )

        self.grid = ttk.Treeview(
            self,
            columns=colunas,
            show="headings"
        )

        self.grid.heading("Codigo", text="Código")
        self.grid.heading("Descricao", text="Descrição")
        self.grid.heading("Fornecedor", text="Fornecedor")
        self.grid.heading("Ata", text="Ata")
        self.grid.heading("Qtd", text="Qtd Licitada")

        self.grid.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
