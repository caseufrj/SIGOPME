import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.entrada_service import EntradaService
from services.fornecedor_service import FornecedorService
from views.components.grid_helper import criar_treeview
from views.components.search_helper import criar_barra_pesquisa
from services.licitacao_service import LicitacaoService
from services.historico_service import HistoricoService

from views.components.masks import (
    aplicar_mascara_data,
    aplicar_mascara_moeda
)
from services.estoque_rastreado_service import (
    EstoqueRastreadoService
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
            "licitacao",
            "nf",
            "serie",
            "data_nf",
            "data_entrada",
            "tipo",
            "fornecedor",
            "valor_total"
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
            "licitacao",
            text="Licitação"
        )
        
        self.grid.heading(
            "nf",
            text="NF"
        )
        
        self.grid.heading(
            "serie",
            text="Série"
        )
        
        self.grid.heading(
            "data_nf",
            text="Data NF"
        )
        
        self.grid.heading(
            "data_entrada",
            text="Data Entrada"
        )
        
        self.grid.heading(
            "tipo",
            text="Tipo"
        )
        
        self.grid.heading(
            "fornecedor",
            text="Fornecedor"
        )
        
        self.grid.heading(
            "valor_total",
            text="Valor Total NF"
        )

        self.grid.column(
            "licitacao",
            width=140
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
            "data_nf",
            width=110
        )
        
        self.grid.column(
            "data_entrada",
            width=110
        )
        
        self.grid.column(
            "tipo",
            width=120
        )
        
        self.grid.column(
            "fornecedor",
            width=250
        )
        
        self.grid.column(
            "valor_total",
            width=120
        )

        self.lbl_total = tk.Label(
            self,
            text="0 registros"
        )

        self.lbl_total.pack(
            pady=5
        )

        self.grid.bind(
            "<<TreeviewSelect>>",
            self.carregar_itens_nf
        )

        frame_itens = tk.LabelFrame(
            self,
            text="Itens da Nota Fiscal"
        )
        
        frame_itens.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        colunas_itens = (
            "codigo",
            "material",
            "lote",
            "serie",
            "validade",
            "quantidade",
            "status"
        )

        frame_grid_itens, self.grid_itens = criar_treeview(
            frame_itens,
            colunas_itens
        )
        
        frame_grid_itens.pack(
            fill="both",
            expand=True
        )

        self.grid_itens.heading(
            "codigo",
            text="Código"
        )
        
        self.grid_itens.heading(
            "material",
            text="Nome Produto"
        )
        
        self.grid_itens.heading(
            "lote",
            text="Lote"
        )
        
        self.grid_itens.heading(
            "serie",
            text="Série Produto"
        )
        
        """self.grid_itens.heading(
            "validade",
            text="Validade"
        )"""
        
        self.grid_itens.heading(
            "quantidade",
            text="Qtd"
        )
        
        self.grid_itens.heading(
            "status",
            text="Status"
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

    def carregar_itens_nf(self, event=None):

        selecionado = self.grid.selection()
    
        if not selecionado:
            return
    
        item = self.grid.item(
            selecionado[0]
        )
    
        numero_nf = item["values"][1]
    
        for linha in self.grid_itens.get_children():
    
            self.grid_itens.delete(
                linha
            )
    
        dados = EntradaService.listar_itens_nf(
            numero_nf
        )
    
        for registro in dados:
    
            self.grid_itens.insert(
                "",
                "end",
                values=registro
            )
            

    def novo(self):

        janela = tk.Toplevel(self)

        janela.title(
            "Nova Entrada"
        )

        janela.geometry(
            "700x800"
        )
        itens_nf = []

        lbl_total_itens = tk.Label(
            janela,
            text="Total dos Itens: R$ 0,00"
        )
        
        lbl_total_itens.pack(
            pady=5
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
            text="Licitação"
        ).pack()
        
        cmb_licitacao = ttk.Combobox(
            janela,
            state="readonly"
        )
        
        cmb_licitacao.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Item da Licitação"
        ).pack()
        
        cmb_item = ttk.Combobox(
            janela,
            state="readonly"
        )
        
        cmb_item.pack(
            fill="x",
            padx=10
        )
       
        def pesquisar_fornecedor(event=None):

            texto = txt_fornecedor.get().strip()
        
            lst_fornecedores.delete(
                0,
                tk.END
            )
        
            if not texto:
                return
        
            fornecedores = (
                FornecedorService.pesquisar_nomes(
                    texto
                )
            )
        
            for fornecedor in fornecedores:
        
                lst_fornecedores.insert(
                    tk.END,
                    fornecedor
                )

        def selecionar_fornecedor(event=None):

            selecionado = (
                lst_fornecedores.curselection()
            )
        
            if not selecionado:
                return
        
            fornecedor = (
                lst_fornecedores.get(
                    selecionado[0]
                )
            )
        
            txt_fornecedor.delete(
                0,
                tk.END
            )
        
            # NOVO
        
            licitacoes = (
                LicitacaoService.listar_licitacoes_fornecedor(
                    fornecedor
                )
            )
        
            cmb_licitacao["values"] = [
                x[0] for x in licitacoes
            ]
        
            txt_fornecedor.insert(
                0,
                fornecedor
            )
        
            lst_fornecedores.delete(
                0,
                tk.END
            )

        txt_fornecedor.bind(
            "<KeyRelease>",
            pesquisar_fornecedor
        )
        
        lst_fornecedores.bind(
            "<Double-Button-1>",
            selecionar_fornecedor
        )

        tk.Label(
            janela,
            text="Valor Total NF"
        ).pack()
        
        txt_valor_nf = tk.Entry(
            janela
        )
               
        aplicar_mascara_moeda(
            txt_valor_nf
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
        
        aplicar_mascara_moeda(
            txt_valor_unitario
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

        item_selecionado = {}
        def carregar_itens_licitacao(event=None):

            numero_licitacao = cmb_licitacao.get()
        
            itens = (
                LicitacaoService.listar_itens_entrada(
                    numero_licitacao
                )
            )
        
            cmb_item["values"] = [
                f"{x[1]} - {x[2]}"
                for x in itens
            ]
        
            item_selecionado["dados"] = itens

        cmb_licitacao.bind(
            "<<ComboboxSelected>>",
            carregar_itens_licitacao
        )

        def selecionar_item(event=None):

            texto = cmb_item.get()
        
            if not texto:
                return
        
            codigo = texto.split(" - ")[0]
        
            for registro in item_selecionado["dados"]:
        
                if registro[1] == codigo:
        
                    txt_codigo.delete(
                        0,
                        tk.END
                    )
        
                    txt_codigo.insert(
                        0,
                        registro[1]
                    )
        
                    txt_material.delete(
                        0,
                        tk.END
                    )
        
                    txt_material.insert(
                        0,
                        registro[2]
                    )
        
                    txt_valor_unitario.delete(
                        0,
                        tk.END
                    )
        
                    txt_valor_unitario.insert(
                        0,
                        str(registro[3])
                    )
        
                    item_selecionado["id"] = registro[0]
        
                    break

        cmb_item.bind(
            "<<ComboboxSelected>>",
            selecionar_item
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
        
                valor_nf = float(
                    txt_valor_nf.get()
                    .replace("R$", "")
                    .replace(".", "")
                    .replace(",", ".")
                    .strip()
                )
        
                valor_unitario = float(
                    txt_valor_unitario.get()
                    .replace("R$", "")
                    .replace(".", "")
                    .replace(",", ".")
                    .strip()
                )
        
            except ValueError:
        
                messagebox.showerror(
                    "SIGOPME",
                    "Valores inválidos."
                )
        
                return

            if not itens_nf:

                messagebox.showwarning(
                    "SIGOPME",
                    "Adicione pelo menos um item na nota."
                )
            
                return

            total_itens = 0

            for item in itens_nf:
            
                total_itens += item["valor_total"]

            if round(total_itens, 2) != round(valor_nf, 2):

                diferenca = (
                    valor_nf - total_itens
                )
            
                messagebox.showerror(
            
                    "SIGOPME",
            
                    f"""Valor da NF não confere.
            
            Valor NF: R$ {valor_nf:,.2f}
            
            Valor dos Itens: R$ {total_itens:,.2f}
            
            Diferença: R$ {diferenca:,.2f}
            """
            
                )
            
                return
        
            nota_id = EntradaService.inserir(
                txt_nf.get(),
                txt_serie.get(),
                txt_data_emissao.get(),
                txt_data_entrada.get(),
                cmb_tipo.get(),
                txt_fornecedor.get(),
                valor_nf,
                txt_observacao.get(
                    "1.0",
                    "end"
                ).strip(),
                cmb_licitacao.get()
            )

            for item in itens_nf:

                HistoricoService.registrar(
            
                    tipo="ENTRADA",
            
                    acao="ITEM_RECEBIDO",
            
                    numero_licitacao=cmb_licitacao.get(),
            
                    fornecedor=txt_fornecedor.get(),
            
                    documento=txt_nf.get(),
            
                    cod_item=item["codigo"],
            
                    nome_material=item["material"],
            
                    lote=item["lote"],
            
                    codigo_unico=item["serie"]
            
                )
            
                EstoqueRastreadoService.inserir(
            
                    item["licitacao_item_id"],
            
                    cmb_licitacao.get(),
            
                    item["codigo"],
            
                    item["material"],
            
                    item["lote"],
            
                    item["serie"],
            
                    txt_nf.get()
            
                )
        
            self.carregar_dados()
        
            janela.destroy()
        
            messagebox.showinfo(
                "SIGOPME",
                "Entrada cadastrada."
            )

        colunas_temp = (
            "codigo",
            "material",
            "lote",
            "serie",
            "validade",
            "quantidade",
            "valor_unitario",
            "valor_total"
        )
        
        frame_temp, grid_temp = criar_treeview(
            janela,
            colunas_temp
        )
        
        frame_temp.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        def incluir_item():

            if not txt_codigo.get():
        
                messagebox.showwarning(
                    "SIGOPME",
                    "Selecione um item."
                )
        
                return
        
            valor_unitario = float(
                txt_valor_unitario.get()
                .replace("R$", "")
                .replace(".", "")
                .replace(",", ".")
                .strip()
            )
        
            quantidade = int(
                txt_quantidade.get()
            )
        
            registro = {

                "licitacao_item_id":
                    item_selecionado["id"],
            
                "codigo":
                    txt_codigo.get(),
            
                "material":
                    txt_material.get(),
            
                "lote":
                    txt_lote.get(),
            
                "serie":
                    txt_serie_produto.get(),
            
                "validade":
                    txt_validade.get(),
            
                "quantidade":
                    quantidade,
            
                "valor_unitario":
                    valor_unitario,
            
                "valor_total":
                    quantidade * valor_unitario
            
            }
        
            itens_nf.append(
                registro
            )
        
            grid_temp.insert(
                "",
                "end",
                values=(
            
                    registro["codigo"],
                    registro["material"],
                    registro["lote"],
                    registro["serie"],
                    registro["validade"],
                    registro["quantidade"],
                    registro["valor_unitario"],
                    registro["valor_total"]
            
                )
            )
        
            txt_lote.delete(0, tk.END)
        
            txt_serie_produto.delete(0, tk.END)
        
            txt_validade.delete(0, tk.END)
        
            txt_quantidade.delete(0, tk.END)

            total = 0

            for item in itens_nf:
            
                total += item["valor_total"]
            
            lbl_total_itens.config(
                text=f"Total dos Itens: R$ {total:,.2f}"
            )

        tk.Button(
            janela,
            text="Incluir Item",
            command=incluir_item
        ).pack(
            pady=5
        )

        grid_temp.heading(
            "codigo",
            text="Código"
        )
        
        grid_temp.heading(
            "material",
            text="Produto"
        )
        
        grid_temp.heading(
            "lote",
            text="Lote"
        )
        
        grid_temp.heading(
            "serie",
            text="Série"
        )
        
        grid_temp.heading(
            "validade",
            text="Validade"
        )
        
        grid_temp.heading(
            "quantidade",
            text="Qtd"
        )

        tk.Button(
            janela,
            text="Salvar",
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

        selecionado = self.grid.selection()
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione uma entrada."
            )
    
            return
    
        confirmar = messagebox.askyesno(
            "SIGOPME",
            "Deseja excluir a entrada?"
        )
    
        if not confirmar:
            return
    
        item = self.grid.item(
            selecionado[0]
        )
    
        id_registro = item["values"][0]
    
        EntradaService.excluir(
            id_registro
        )
    
        self.carregar_dados()
    
        messagebox.showinfo(
            "SIGOPME",
            "Entrada excluída."
        )

    def carregar_itens_nf(self, event=None):

        selecionado = self.grid.selection()
    
        if not selecionado:
            return
    
        item = self.grid.item(
            selecionado[0]
        )
    
        nf = item["values"][1]
    
        for linha in self.grid_itens.get_children():
            self.grid_itens.delete(linha)
    
        dados = EntradaService.listar_itens_nf(
            nf
        )
    
        for registro in dados:
    
            self.grid_itens.insert(
                "",
                "end",
                values=registro
            )

    
