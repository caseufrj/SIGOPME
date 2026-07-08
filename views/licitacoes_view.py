import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

from services.importacao_excel import ImportacaoExcelService
from services.licitacao_service import LicitacaoService


class LicitacoesView(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Licitações")
        self.geometry("1200x700")

        self.criar_componentes()
        self.carregar_dados()

    def criar_componentes(self):

        frm_filtro = tk.Frame(self)
        frm_filtro.pack(fill="x", padx=10, pady=10)

        tk.Label(frm_filtro, text="Pesquisar").pack(side="left")

        btn_pesquisar = tk.Button(
            frm_filtro,
            text="Pesquisar",
            command=self.pesquisar
        )

        btn_pesquisar.pack(side="left")
        self.txt_pesquisa = tk.Entry(
            frm_filtro,
            width=50
        )
        
        self.txt_pesquisa.pack(
            side="left",
            padx=10
        )
        
        self.txt_pesquisa.bind(
            "<Return>",
            lambda event: self.pesquisar()
        )

        btn_importar = tk.Button(
            frm_filtro,
            text="Importar Excel",
            command=self.importar_excel
        )
        
        btn_importar.pack(side="left", padx=10)

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
        self.lbl_total = tk.Label(
            self,
            text="0 registros"
        )
        
        self.lbl_total.pack(
            pady=5
        )

    def importar_excel(self):

        arquivo = filedialog.askopenfilename(
            title="Selecionar planilha",
            filetypes=[
                ("Excel", "*.xlsx")
            ]
        )
    
        if not arquivo:
            return
    
        quantidade = ImportacaoExcelService.importar_licitacoes(
            arquivo
        )
        self.carregar_dados()
    
        messagebox.showinfo(
            "Importação",
            f"{quantidade} registros importados."
        )

    def carregar_dados(self):

        registros = LicitacaoService.listar_todos()
    
        self.preencher_grid(registros)
        
    def pesquisar(self):

        texto = self.txt_pesquisa.get().strip()
    
        if texto == "":
            registros = LicitacaoService.listar_todos()
        else:
            registros = LicitacaoService.pesquisar(texto)
    
        self.preencher_grid(registros)

    def preencher_grid(self, registros):

        for item in self.grid.get_children():
            self.grid.delete(item)
    
        for registro in registros:
    
            self.grid.insert(
                "",
                "end",
                values=registro
            )
    
        self.lbl_total.config(
            text=f"{len(registros)} registros encontrados"
        )

