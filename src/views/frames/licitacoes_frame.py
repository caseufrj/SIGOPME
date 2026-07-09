import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.licitacao_service import LicitacaoService

class LicitacoesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()
        self.carregar_dados()

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
            text="Novo",
            command=self.novo
        ).pack(
            side="left",
            padx=5
        )
        tk.Button(
            barra_acoes,
            text="Editar",
            command=self.editar
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
            "id",
        
            "licitacao",
            "ata",
            "fornecedor",
            "tipo",
        
            "codigo_item",
            "material",
        
            "qtd_licitada",
            "valor",
        
            "saldo_pedido",
            "saldo_financeiro",
        
            "consignacao",
            "retirado",
            "utilizado",
            "em_pagamento",
            "pago"
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
        self.grid.heading(
            "id",
            text="Id"
        )
        
        self.grid.column(
            "id",
            width=0,
            stretch=False
        )

    def novo(self):
    
        janela = tk.Toplevel(self)
    
        janela.title("Nova Licitação")
    
        janela.geometry("500x400")
    
        tk.Label(
            janela,
            text="Número Licitação"
        ).pack()
    
        txt_licitacao = tk.Entry(janela)
        txt_licitacao.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Ata"
        ).pack()
    
        txt_ata = tk.Entry(janela)
        txt_ata.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Código"
        ).pack()
    
        txt_codigo = tk.Entry(janela)
        txt_codigo.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Descrição"
        ).pack()
    
        txt_descricao = tk.Entry(janela)
        txt_descricao.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Fornecedor"
        ).pack()
    
        txt_fornecedor = tk.Entry(janela)
        txt_fornecedor.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Quantidade"
        ).pack()
    
        txt_quantidade = tk.Entry(janela)
        txt_quantidade.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Valor Unitário"
        ).pack()
    
        txt_valor = tk.Entry(janela)
        txt_valor.pack(fill="x", padx=10)
    
        def salvar():

            try:
        
                quantidade = int(
                    txt_quantidade.get()
                )
        
                valor = float(
                    txt_valor.get().replace(",", ".")
                )
        
            except ValueError:
        
                messagebox.showerror(
                    "Erro",
                    "Quantidade e Valor devem ser numéricos."
                )
        
                return
        
            LicitacaoService.inserir(
                txt_licitacao.get(),
                txt_ata.get(),
                txt_fornecedor.get(),
                txt_tipo.get(),
                txt_codigo.get(),
                txt_material.get(),
                quantidade,
                valor
            )
        
            self.carregar_dados()
        
            janela.destroy()
        
            messagebox.showinfo(
                "SIGOPME",
                "Licitação cadastrada."
            )
    
            self.carregar_dados()
    
            janela.destroy()
    
            messagebox.showinfo(
                "SIGOPME",
                "Licitação cadastrada."
            )
    
        tk.Button(
            janela,
            text="Salvar",
            command=salvar
        ).pack(
            pady=10
        )
    
    
    def carregar_dados(self):
    
        for item in self.grid.get_children():
            self.grid.delete(item)
    
        registros = LicitacaoService.listar_todos()
    
        for registro in registros:
    
            self.grid.insert(
                "",
                "end",
                values=registro
            )
    
        self.lbl_total.config(
            text=f"{len(registros)} registros"
        )
