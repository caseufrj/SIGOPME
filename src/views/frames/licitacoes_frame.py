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

        self.txt_pesquisa = tk.Entry(
            barra_acoes,
            width=40
        )
        
        self.txt_pesquisa.pack(
            side="right"
        )
        
        tk.Label(
            barra_acoes,
            text="Pesquisar:"
        ).pack(
            side="right"
        )

        # ==========================
        # GRID SUPERIOR - LICITAÇÕES
        # ==========================
        
        lbl_superior = tk.Label(
            self,
            text="Licitações"
        )
        lbl_superior.pack()
        
        colunas_licitacoes = (
            "id",
            "licitacao",
            "ata",
            "fornecedor",
            "tipo",
            "consignado",
            "valor_total"
        )
        
        frame_licitacoes, self.grid_licitacoes = criar_treeview(
            self,
            colunas_licitacoes
        )
        
        frame_licitacoes.pack(
            fill="x",
            padx=10,
            pady=5
        )
        
        self.grid_licitacoes.heading("id", text="Id")
        self.grid_licitacoes.heading("licitacao", text="Licitação")
        self.grid_licitacoes.heading("ata", text="Ata")
        self.grid_licitacoes.heading("fornecedor", text="Fornecedor")
        self.grid_licitacoes.heading("tipo", text="Tipo Licitação")
        self.grid_licitacoes.heading("consignado", text="Consignado?")
        self.grid_licitacoes.heading("valor_total", text="Valor Total Pregão")
        
        self.grid_licitacoes.column(
            "id",
            width=0,
            stretch=False
        )
        
        self.grid_licitacoes.column(
            "licitacao",
            width=120
        )
        
        self.grid_licitacoes.column(
            "ata",
            width=100
        )
        
        self.grid_licitacoes.column(
            "fornecedor",
            width=250
        )
        
        self.grid_licitacoes.column(
            "tipo",
            width=130
        )
        
        self.grid_licitacoes.column(
            "consignado",
            width=90
        )
        
        self.grid_licitacoes.column(
            "valor_total",
            width=150
        )
        
        # Duplo clique em qualquer lugar da linha
        self.grid_licitacoes.bind(
            "<Double-1>",
            self.abrir_licitacao
        )
        
        # ==========================
        # TÍTULO DOS ITENS
        # ==========================
        
        self.lbl_detalhe = tk.Label(
            self,
            text="Itens da Licitação"
        )
        
        self.lbl_detalhe.pack(
            pady=(15, 5)
        )

        # ==========================
        # BOTÕES ITENS
        # ==========================

        barra_itens = tk.Frame(self)

        barra_itens.pack(
            fill="x",
            padx=10,
            pady=5
        )
        
        self.btn_novo_item = tk.Button(
            barra_itens,
            text="Novo Item",
            command=self.novo_item
        )
        
        self.btn_novo_item.pack(
            side="left",
            padx=5
        )
        
        self.btn_editar_item = tk.Button(
            barra_itens,
            text="Editar Item",
            command=self.editar_item,
            state="disabled"
        )
        
        self.btn_editar_item.pack(
            side="left",
            padx=5
        )
        
        self.btn_excluir_item = tk.Button(
            barra_itens,
            text="Excluir Item",
            command=self.excluir_item,
            state="disabled"
        )
        
        self.btn_excluir_item.pack(
            side="left",
            padx=5
        )
        
        # ==========================
        # GRID INFERIOR - ITENS
        # ==========================
        
        colunas_itens = (
            "item",
            "material",
            "qtd_licitada",
            "valor_unit",
            "saldo_pedido",
            "saldo_financeiro",
            "consignacao",
            "retirado",
            "utilizado",
            "em_pagamento",
            "pago"
        )
        
        frame_itens, self.grid_itens = criar_treeview(
            self,
            colunas_itens
        )
        
        frame_itens.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=5
        )
        
        self.grid_itens.heading("item", text="Item")
        self.grid_itens.heading("material", text="Nome Material")
        self.grid_itens.heading("qtd_licitada", text="Qtd Licitada")
        self.grid_itens.heading("valor_unit", text="Valor Unit.")
        self.grid_itens.heading("saldo_pedido", text="Saldo Pedido")
        self.grid_itens.heading("saldo_financeiro", text="Saldo Financeiro")
        self.grid_itens.heading("consignacao", text="Consignação")
        self.grid_itens.heading("retirado", text="Retirado")
        self.grid_itens.heading("utilizado", text="Utilizado")
        self.grid_itens.heading("em_pagamento", text="Em Pagamento")
        self.grid_itens.heading("pago", text="Pago")
        
        self.grid_itens.column(
            "item",
            width=80
        )
        
        self.grid_itens.column(
            "material",
            width=350
        )
        
        self.grid_itens.column(
            "qtd_licitada",
            width=100
        )
        
        self.grid_itens.column(
            "valor_unit",
            width=100
        )
        
        self.grid_itens.column(
            "saldo_pedido",
            width=100
        )
        
        self.grid_itens.column(
            "saldo_financeiro",
            width=120
        )
        
        self.grid_itens.column(
            "consignacao",
            width=100
        )
        
        self.grid_itens.column(
            "retirado",
            width=100
        )
        
        self.grid_itens.column(
            "utilizado",
            width=100
        )
        
        self.grid_itens.column(
            "em_pagamento",
            width=120
        )
        
        self.grid_itens.column(
            "pago",
            width=100
        )

        self.grid_itens.bind(
            "<<TreeviewSelect>>",
            self.item_selecionado
        )

    def novo(self):

        janela = tk.Toplevel(self)
    
        janela.title("Nova Licitação")
    
        janela.geometry("500x350")
    
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
            text="Consignado?"
        ).pack()
    
        cbo_consignado = ttk.Combobox(
            janela,
            values=["SIM", "NÃO"],
            state="readonly"
        )
    
        cbo_consignado.pack(
            fill="x",
            padx=10
        )
    
        def salvar():
    
            LicitacaoService.inserir_licitacao(
                txt_licitacao.get(),
                txt_ata.get(),
                txt_fornecedor.get(),
                txt_tipo.get(),
                cbo_consignado.get()
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
    
        for item in self.grid_licitacoes.get_children():
            self.grid_licitacoes.delete(item)
    
        registros = LicitacaoService.listar_resumo_licitacoes()
    
        for registro in registros:
    
            self.grid_licitacoes.insert(
                "",
                "end",
                values=registro
            )
    
        self.lbl_total.config(
            text=f"{len(registros)} registros"
        )

    def editar(self):

        selecionado = self.grid_licitacoes.selection()
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione um registro para editar."
            )
    
            return
    
        item = self.grid_licitacoes.item(
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
            consignado
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

            LicitacaoService.atualizar_licitacao(
                id_registro,
                txt_licitacao.get(),
                txt_ata.get(),
                txt_fornecedor.get(),
                txt_tipo.get(),
                cbo_consignado.get()
            )
        
            self.carregar_dados()
        
            janela.destroy()
        
            messagebox.showinfo(
                "SIGOPME",
                "Licitação atualizada com sucesso."
            )
    
        tk.Button(
            janela,
            text="Salvar Alterações",
            command=salvar_edicao
        ).pack(
            pady=10
        )
        
    def excluir(self):

        selecionado = self.grid_licitacoes.selection()
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione um registro para excluir."
            )
    
            return
    
        item = self.grid_licitacoes.item(
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
    
        confirmar = messagebox.askyesno(
            "SIGOPME",
            f"Deseja excluir a licitação {item['values'][1]}?"
        )

    def item_selecionado(self, event):

        selecionado = self.grid_itens.selection()
    
        if selecionado:
    
            self.btn_editar_item.config(
                state="normal"
            )
    
            self.btn_excluir_item.config(
                state="normal"
            )
    
        else:
    
            self.btn_editar_item.config(
                state="disabled"
            )
    
            self.btn_excluir_item.config(
                state="disabled"
            )

    def novo_item(self):

        selecionado = self.grid_licitacoes.selection()
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione uma licitação primeiro."
            )
    
            return

   def editar_item(self):
    
        selecionado = self.grid_itens.selection()
    
        if not selecionado:
    
            return
    
        item = self.grid_itens.item(
            selecionado[0]
        )
    
        id_item = item["values"][0] 

    def excluir_item(self):

        selecionado = self.grid_itens.selection()
    
        if not selecionado:
            return
    
        item = self.grid_itens.item(
            selecionado[0]
        )
    
        id_item = item["values"][0]
    
        confirmar = messagebox.askyesno(
            "SIGOPME",
            "Deseja excluir este item?"
        )
    
        if not confirmar:
            return
    
        LicitacaoService.excluir_item(
            id_item
        )

