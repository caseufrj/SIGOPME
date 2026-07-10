import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.entrada_service import EntradaService

from views.components.grid_helper import criar_treeview
from views.components.search_helper import criar_barra_pesquisa
from services.licitacao_service import LicitacaoService

from views.components.masks import (
    aplicar_mascara_data,
    aplicar_mascara_moeda
)

class EntradasFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()
        self.carregar_dados()

    def criar_componentes(self):

        titulo = tk.Label(
            self,
            text="Entradas",
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

        frame_pesquisa, self.txt_pesquisa = criar_barra_pesquisa(
            barra
        )

        frame_pesquisa.pack(
            side="right"
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

        colunas = (
            "id",
            "nf",
            "serie",
            "data",
            "tipo",
            "fornecedor",
            "codigo",
            "material",
            "quantidade"
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

        self.grid.heading("id", text="Id")
        self.grid.heading("nf", text="NF")
        self.grid.heading("serie", text="Série")
        self.grid.heading("data", text="Data Entrada")
        self.grid.heading("tipo", text="Tipo Entrada")
        self.grid.heading("fornecedor", text="Fornecedor")
        self.grid.heading("codigo", text="Código Item")
        self.grid.heading("material", text="Nome Material")
        self.grid.heading("quantidade", text="Quantidade")

        self.grid.column(
            "id",
            width=0,
            stretch=False
        )

        self.grid.column(
            "nf",
            width=100
        )

        self.grid.column(
            "serie",
            width=80
        )

        self.grid.column(
            "data",
            width=120
        )

        self.grid.column(
            "tipo",
            width=130
        )

        self.grid.column(
            "fornecedor",
            width=250
        )

        self.grid.column(
            "codigo",
            width=100
        )

        self.grid.column(
            "material",
            width=300
        )

        self.grid.column(
            "quantidade",
            width=100
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

        dados = EntradaService.listar_todos()

        for entrada in dados:

            self.grid.insert(
                "",
                "end",
                values=entrada
            )

        self.lbl_total.config(
            text=f"{len(dados)} registros"
        )

    def novo(self):

        janela = tk.Toplevel(self)

        janela.title(
            "Nova Entrada"
        )

        janela.geometry(
            "700x800"
        )

        tk.Label(
            janela,
            text="Nota Fiscal"
        ).pack()

        txt_nf = tk.Entry(janela)

        txt_nf.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Série"
        ).pack()

        txt_serie = tk.Entry(janela)

        txt_serie.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Data Emissão"
        ).pack()

        txt_data_emissao = tk.Entry(janela)
        aplicar_mascara_data(
            txt_data_emissao
        )


        txt_data_emissao.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Data Entrada"
        ).pack()

        txt_data_entrada = tk.Entry(janela)
         aplicar_mascara_data(
            txt_data_entrada
        )

        txt_data_entrada.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Tipo Entrada"
        ).pack()

        cmb_tipo = ttk.Combobox(
            janela,
            values=[
                "CONSIGNADO",
                "VENDA"
            ],
            state="readonly"
        )

        cmb_tipo.pack(
            fill="x",
            padx=10
        )

        cmb_tipo.set(
            "CONSIGNADO"
        )

        tk.Label(
            janela,
            text="Fornecedor"
        ).pack()

        txt_fornecedor = tk.Entry(janela)

        txt_fornecedor.pack(
            fill="x",
            padx=10
        )
        
        lst_fornecedores = tk.Listbox(
            janela,
            height=5
        )
        
        lst_fornecedores.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Valor Total NF"
        ).pack()
        
        txt_valor_nf = tk.Entry(
            janela
        )
        
        txt_valor_nf.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Código Item"
        ).pack()

        txt_codigo = tk.Entry(janela)

        txt_codigo.pack(
            fill="x",
            padx=10
        )
        
        tk.Label(
            janela,
            text="Nome Material"
        ).pack()

        txt_material = tk.Entry(janela)

        txt_material.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Valor Unitário"
        ).pack()
        
        txt_valor_unitario = tk.Entry(
            janela
        )
        
        txt_valor_unitario.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Lote"
        ).pack()
        
        txt_lote = tk.Entry(
            janela
        )
        
        txt_lote.pack(
            fill="x",
            padx=10
        )
        
        tk.Label(
            janela,
            text="Série Produto"
        ).pack()
        
        txt_serie_produto = tk.Entry(
            janela
        )
        
        txt_serie_produto.pack(
            fill="x",
            padx=10
        )
        
        tk.Label(
            janela,
            text="Data Validade"
        ).pack()
        
        txt_validade = tk.Entry(
            janela
        )
        aplicar_mascara_data(
            txt_validade
        )
        
        txt_validade.pack(
            fill="x",
            padx=10
        )

        def buscar_item(event=None):

            codigo = txt_codigo.get().strip()
        
            if not codigo:
                return
        
            dados = LicitacaoService.obter_por_codigo(
                codigo
            )
        
            if not dados:
                return
        
            fornecedor, material, valor_unitario = dados
        
            txt_fornecedor.delete(
                0,
                tk.END
            )
        
            txt_fornecedor.insert(
                0,
                fornecedor
            )
        
            txt_material.delete(
                0,
                tk.END
            )
        
            txt_material.insert(
                0,
                material
            )

            txt_valor_unitario.delete(
                0,
                tk.END
            )
            
            txt_valor_unitario.insert(
                0,
                str(valor_unitario)
            )

        tk.Label(
            janela,
            text="Quantidade"
        ).pack()

        txt_quantidade = tk.Entry(janela)

        txt_quantidade.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Observação"
        ).pack()

        txt_observacao = tk.Text(
            janela,
            height=4
        )

        txt_observacao.pack(
            fill="x",
            padx=10
        )

        txt_codigo.bind(
            "<FocusOut>",
            buscar_item
        )

        def salvar():

            try:

                quantidade = int(
                    txt_quantidade.get()
                )

            except ValueError:

                messagebox.showerror(
                    "SIGOPME",
                    "Quantidade inválida."
                )

                return

            EntradaService.inserir(
                txt_nf.get(),
                txt_serie.get(),
                txt_data_emissao.get(),
                txt_data_entrada.get(),
                cmb_tipo.get(),
                txt_fornecedor.get(),
                txt_codigo.get(),
                txt_material.get(),
                quantidade,
                txt_observacao.get(
                    "1.0",
                    "end"
                ).strip()
            )

            self.carregar_dados()

            janela.destroy()

            messagebox.showinfo(
                "SIGOPME",
                "Entrada cadastrada."
            )

        tk.Button(
            janela,
            text="Salvar"
            ,
            command=salvar
        ).pack(
            pady=10
        )

    def editar(self):

        messagebox.showinfo(
            "SIGOPME",
            "Editar em desenvolvimento."
        )
    
    
    def excluir(self):
    
        messagebox.showinfo(
            "SIGOPME",
            "Excluir em desenvolvimento."
        )
