import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.licitacao_service import LicitacaoService
from views.components.grid_helper import criar_treeview


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
            text="Excluir",
            command=self.excluir
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            barra_acoes,
            text="Pesquisar:"
        ).pack(
            side="right",
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
        self.grid.heading("licitacao", text="Licitação")
        self.grid.heading("ata", text="Ata")
        self.grid.heading("fornecedor", text="Fornecedor")
        self.grid.heading("tipo", text="Tipo Licitação")
        self.grid.heading("codigo_item", text="Código Item")
        self.grid.heading("material", text="Nome Material")
        self.grid.heading("qtd_licitada", text="Qtd Licitada")
        self.grid.heading("valor", text="Valor Unit.")
        self.grid.heading("saldo_pedido", text="Saldo Pedido")
        self.grid.heading("saldo_financeiro", text="Saldo Financeiro")
        self.grid.heading("consignacao", text="Consignação")
        self.grid.heading("retirado", text="Retirado")
        self.grid.heading("utilizado", text="Utilizado")
        self.grid.heading("em_pagamento", text="Em Pagamento")
        self.grid.heading("pago", text="Pago")

        self.grid.column(
            "id",
            width=0,
            stretch=False
        )

        self.grid.column(
            "licitacao",
            width=120
        )

        self.grid.column(
            "ata",
            width=100
        )

        self.grid.column(
            "fornecedor",
            width=250
        )

        self.grid.column(
            "tipo",
            width=130
        )

        self.grid.column(
            "codigo_item",
            width=100
        )

        self.grid.column(
            "material",
            width=350
        )

        self.grid.column(
            "qtd_licitada",
            width=110
        )

        self.grid.column(
            "valor",
            width=100
        )

        self.grid.column(
            "saldo_pedido",
            width=120
        )

        self.grid.column(
            "saldo_financeiro",
            width=140
        )

        self.grid.column(
            "consignacao",
            width=100
        )

        self.grid.column(
            "retirado",
            width=100
        )

        self.grid.column(
            "utilizado",
            width=100
        )

        self.grid.column(
            "em_pagamento",
            width=120
        )

        self.grid.column(
            "pago",
            width=100
        )

        self.lbl_total = tk.Label(
            self,
            text="0 registros"
        )

        self.lbl_total.pack(
            pady=5
        )

    def novo(self):

        janela = tk.Toplevel(self)
    
        janela.title("Nova Licitação")
    
        janela.geometry("600x500")
    
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
            text="Fornecedor"
        ).pack()
    
        txt_fornecedor = tk.Entry(janela)
        txt_fornecedor.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Tipo Licitação"
        ).pack()
    
        txt_tipo = tk.Entry(janela)
        txt_tipo.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Código Item"
        ).pack()
    
        txt_codigo_item = tk.Entry(janela)
        txt_codigo_item.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Nome Material"
        ).pack()
    
        txt_material = tk.Entry(janela)
        txt_material.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Quantidade Licitada"
        ).pack()
    
        txt_qtd_licitada = tk.Entry(janela)
        txt_qtd_licitada.pack(fill="x", padx=10)
    
        tk.Label(
            janela,
            text="Valor Unitário"
        ).pack()
    
        txt_valor = tk.Entry(janela)
        txt_valor.pack(fill="x", padx=10)
    
        def salvar():
    
            try:
    
                qtd_licitada = int(
                    txt_qtd_licitada.get()
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
                txt_codigo_item.get(),
                txt_material.get(),
                qtd_licitada,
                valor
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

    def editar(self):

        selecionado = self.grid.selection()
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione um registro para editar."
            )
    
            return
    
        item = self.grid.item(
            selecionado[0]
        )
    
        id_registro = item["values"][0]
    
        dados = LicitacaoService.obter_por_id(
            id_registro
        )
    
        if not dados:
    
            messagebox.showerror(
                "SIGOPME",
                "Registro não encontrado."
            )
    
            return
    
        (
            _id,
            licitacao,
            ata,
            fornecedor,
            tipo,
            codigo_item,
            nome_material,
            qtd_licitada,
            valor
        ) = dados
    
        janela = tk.Toplevel(self)
    
        janela.title("Editar Licitação")
    
        janela.geometry("600x500")
    
        tk.Label(janela, text="Licitação").pack()
        txt_licitacao = tk.Entry(janela)
        txt_licitacao.pack(fill="x", padx=10)
        txt_licitacao.insert(0, licitacao)
    
        tk.Label(janela, text="Ata").pack()
        txt_ata = tk.Entry(janela)
        txt_ata.pack(fill="x", padx=10)
        txt_ata.insert(0, ata)
    
        tk.Label(janela, text="Fornecedor").pack()
        txt_fornecedor = tk.Entry(janela)
        txt_fornecedor.pack(fill="x", padx=10)
        txt_fornecedor.insert(0, fornecedor)
    
        tk.Label(janela, text="Tipo Licitação").pack()
        txt_tipo = tk.Entry(janela)
        txt_tipo.pack(fill="x", padx=10)
        txt_tipo.insert(0, tipo)
    
        tk.Label(janela, text="Código Item").pack()
        txt_codigo_item = tk.Entry(janela)
        txt_codigo_item.pack(fill="x", padx=10)
        txt_codigo_item.insert(0, codigo_item)
    
        tk.Label(janela, text="Nome Material").pack()
        txt_material = tk.Entry(janela)
        txt_material.pack(fill="x", padx=10)
        txt_material.insert(0, nome_material)
    
        tk.Label(janela, text="Qtd Licitada").pack()
        txt_qtd = tk.Entry(janela)
        txt_qtd.pack(fill="x", padx=10)
        txt_qtd.insert(0, qtd_licitada)
    
        tk.Label(janela, text="Valor Unitário").pack()
        txt_valor = tk.Entry(janela)
        txt_valor.pack(fill="x", padx=10)
        txt_valor.insert(0, valor)
    
        def salvar_edicao():
    
            try:
    
                quantidade = int(
                    txt_qtd.get()
                )
    
                valor_unitario = float(
                    txt_valor.get().replace(",", ".")
                )
    
            except ValueError:
    
                messagebox.showerror(
                    "Erro",
                    "Quantidade e Valor inválidos."
                )
    
                return
    
            LicitacaoService.atualizar(
                id_registro,
                txt_licitacao.get(),
                txt_ata.get(),
                txt_fornecedor.get(),
                txt_tipo.get(),
                txt_codigo_item.get(),
                txt_material.get(),
                quantidade,
                valor_unitario
            )
    
            self.carregar_dados()
    
            janela.destroy()
    
            messagebox.showinfo(
                "SIGOPME",
                "Registro atualizado com sucesso."
            )
    
        tk.Button(
            janela,
            text="Salvar Alterações",
            command=salvar_edicao
        ).pack(
            pady=10
        )
        
    def excluir(self):

        selecionado = self.grid.selection()
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione um registro para excluir."
            )
    
            return
    
        item = self.grid.item(
            selecionado[0]
        )
    
        id_registro = item["values"][0]
    
        confirmar = messagebox.askyesno(
            "SIGOPME",
            "Deseja realmente excluir este registro?"
        )
    
        if not confirmar:
            return
    
        LicitacaoService.excluir(
            id_registro
        )
    
        self.carregar_dados()
    
        messagebox.showinfo(
            "SIGOPME",
            "Registro excluído com sucesso."
        )
