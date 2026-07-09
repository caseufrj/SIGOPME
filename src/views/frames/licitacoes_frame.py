import tkinter as tk
from tkinter import ttk


class LicitacoesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()

    def criar_componentes(self):

        titulo = tk.Label(
            self,
            text="Licitações",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        barra_acoes = tk.Frame(self)

        barra_acoes.pack(
            fill="x",
            padx=10,
            pady=5
        )

        tk.Button(
            barra_acoes,
            text="Novo"
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            barra_acoes,
            text="Editar"
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            barra_acoes,
            text="Excluir"
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            barra_acoes,
            text="Pesquisar:"
        ).pack(
            side="left",
            padx=(20, 5)
        )

        self.txt_pesquisa = tk.Entry(
            barra_acoes,
            width=40
        )

        self.txt_pesquisa.pack(
            side="left"
        )

        colunas = (
            "licitacao",
            "ata",
            "codigo",
            "descricao",
            "fornecedor",
            "quantidade",
            "valor"
        )

        self.grid = ttk.Treeview(
            self,
            columns=colunas,
            show="headings"
        )

        self.grid.heading(
            "licitacao",
            text="Licitação"
        )

        self.grid.heading(
            "ata",
            text="Ata"
        )

        self.grid.heading(
            "codigo",
            text="Código"
        )

        self.grid.heading(
            "descricao",
            text="Descrição"
        )

        self.grid.heading(
            "fornecedor",
            text="Fornecedor"
        )

        self.grid.heading(
            "quantidade",
            text="Qtd."
        )

        self.grid.heading(
            "valor",
            text="Valor Unit."
        )

        self.grid.column(
            "descricao",
            width=350
        )

        self.grid.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.lbl_total = tk.Label(
            self,
            text="0 registros"
        )

        self.lbl_total.pack(
            pady=5
        )
