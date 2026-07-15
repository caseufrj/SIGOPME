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

from services.nota_itens_service import (
    NotaItensServicelicitacao.bin
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

    item_selecionado = {}
        
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
        
        janela.state("zoomed")

        canvas = tk.Canvas(
            janela
        )
        
        scroll = ttk.Scrollbar(
            janela,
            orient="vertical",
            command=canvas.yview
        )
        
        frame_conteudo = tk.Frame(
            canvas
        )
        
        frame_conteudo.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window(
            (0, 0),
            window=frame_conteudo,
            anchor="nw"
        )
        
        canvas.configure(
            yscrollcommand=scroll.set
        )
        
        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )
        
        scroll.pack(
            side="right",
            fill="y"
        )

        def _mousewheel(event):

            canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )
        
        canvas.bind_all(
            "<MouseWheel>",
            _mousewheel
        )

        
        itens_nf = []
        
        frame_nota = ttk.LabelFrame(
            frame_conteudo,
            text="Dados da Nota Fiscal"
        )
        
        frame_nota.pack(
            fill="x",
            padx=10,
            pady=5
        )
        
        frame_nota.columnconfigure(
            0,
            weight=1
        )
        
        frame_nota.columnconfigure(
            1,
            weight=1
        )

        tk.Label(
            frame_nota,
            text="NF"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )
        
        txt_nf = tk.Entry(
            frame_nota
        )
        
        txt_nf.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )
        
        tk.Label(
            frame_nota,
            text="Série"
        ).grid(
            row=0,
            column=1,
            sticky="w"
        )
        
        txt_serie = tk.Entry(
            frame_nota
        )
        
        txt_serie.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            frame_nota,
            text="Data Emissão"
        ).grid(
            row=2,
            column=0,
            sticky="w"
        )
        
        txt_data_emissao = tk.Entry(
            frame_nota
        )
        
        aplicar_mascara_data(
            txt_data_emissao
        )
        
        txt_data_emissao.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )
        
        tk.Label(
            frame_nota,
            text="Data Entrada"
        ).grid(
            row=2,
            column=1,
            sticky="w"
        )
        
        txt_data_entrada = tk.Entry(
            frame_nota
        )
        
        aplicar_mascara_data(
            txt_data_entrada
        )
        
        txt_data_entrada.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            frame_nota,
            text="Tipo Entrada"
        ).grid(
            row=4,
            column=0,
            sticky="w"
        )
        
        cmb_tipo = ttk.Combobox(
            frame_nota,
            values=[
                "CONSIGNADO",
                "VENDA"
            ],
            state="readonly"
        )
        
        cmb_tipo.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )
        
        cmb_tipo.set(
            "CONSIGNADO"
        )
        
        tk.Label(
            frame_nota,
            text="Licitação"
        ).grid(
            row=4,
            column=1,
            sticky="w"
        )
        
        cmb_licitacao = ttk.Combobox(
            frame_nota,
            state="readonly"
        )
        
        cmb_licitacao.grid(
            row=5,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            frame_nota,
            text="Fornecedor"
        ).grid(
            row=6,
            column=0,
            sticky="w"
        )
        
        txt_fornecedor = tk.Entry(
            frame_nota
        )
        
        txt_fornecedor.grid(
            row=7,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=5,
            pady=5
        )

        lst_fornecedores = tk.Listbox(
            frame_nota,
            height=3
        )
        
        lst_fornecedores.grid(
            row=8,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            frame_nota,
            text="Valor Total NF"
        ).grid(
            row=9,
            column=0,
            sticky="w"
        )
        
        txt_valor_nf = tk.Entry(
            frame_nota
        )
        
        aplicar_mascara_moeda(
            txt_valor_nf
        )
        
        txt_valor_nf.grid(
            row=10,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )

        frame_item = ttk.LabelFrame(
            frame_conteudo,
            text="Item da Nota"
        )
        
        frame_item.pack(
            fill="x",
            padx=10,
            pady=5
        )
        
        frame_item.columnconfigure(
            0,
            weight=1
        )
        
        frame_item.columnconfigure(
            1,
            weight=1
        )

        tk.Label(
            frame_item,
            text="Item da Licitação"
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )
        
        cmb_item = ttk.Combobox(
            frame_item,
            state="readonly"
        )
        
        cmb_item.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )

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
        
                    item_selecionado["id"] = registro[0]
        
                    item_selecionado["codigo"] = registro[1]
        
                    item_selecionado["material"] = registro[2]
        
                    item_selecionado["valor_unitario"] = registro[3]
        
                    txt_valor_unitario.delete(
                        0,
                        tk.END
                    )
        
                    txt_valor_unitario.insert(
                        0,
                        str(registro[3])
                    )
        
                    break
            
        
        tk.Label(
            frame_item,
            text="Quantidade"
        ).grid(
            row=0,
            column=1,
            sticky="w"
        )
        
        txt_quantidade = tk.Entry(
            frame_item
        )
        
        txt_quantidade.grid(
            row=1,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            frame_item,
            text="Código Item"
        ).grid(
            row=2,
            column=0,
            sticky="w"
        )
        
        txt_codigo = tk.Entry(
            frame_item
        )
        
        txt_codigo.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )
        
        tk.Label(
            frame_item,
            text="Valor Unitário"
        ).grid(
            row=2,
            column=1,
            sticky="w"
        )
        
        txt_valor_unitario = tk.Entry(
            frame_item
        )
        
        aplicar_mascara_moeda(
            txt_valor_unitario
        )
        
        txt_valor_unitario.grid(
            row=3,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            frame_item,
            text="Lote"
        ).grid(
            row=4,
            column=0,
            sticky="w"
        )
        
        txt_lote = tk.Entry(
            frame_item
        )
        
        txt_lote.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )
        
        tk.Label(
            frame_item,
            text="Série Produto"
        ).grid(
            row=4,
            column=1,
            sticky="w"
        )
        
        txt_serie_produto = tk.Entry(
            frame_item
        )
        
        txt_serie_produto.grid(
            row=5,
            column=1,
            sticky="ew",
            padx=5,
            pady=5
        )

        tk.Label(
            frame_item,
            text="Data Validade"
        ).grid(
            row=6,
            column=0,
            sticky="w"
        )
        
        txt_validade = tk.Entry(
            frame_item
        )
        
        aplicar_mascara_data(
            txt_validade
        )
        
        txt_validade.grid(
            row=7,
            column=0,
            sticky="ew",
            padx=5,
            pady=5
        )

        lbl_total_itens = tk.Label(
            frame_conteudo,
            text="Total dos Itens: R$ 0,00",
            font=("Arial", 10, "bold")
        )
        
        lbl_total_itens.pack(
            pady=5
        )

        frame_botoes_itens = tk.Frame(
            frame_conteudo
        )
        
        frame_botoes_itens.pack(
            fill="x",
            padx=10,
            pady=5
        )

        frame_botoes_itens.tkraise()
        
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

                NotaItensService.inserir(
            
                    nota_id,
            
                    item["codigo"],
            
                    item["material"],
            
                    item["quantidade"],
            
                    item["valor_unitario"],
            
                    item["valor_total"]
            
                )
            
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
            frame_conteudo,
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
                    item_selecionado["codigo"],
                
                "material":
                    item_selecionado["material"],
            
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

        grid_temp.heading(
            "valor_unitario",
            text="Valor Unit."
        )
        
        grid_temp.heading(
            "valor_total",
            text="Valor Total"
        )

        tk.Label(
            frame_conteudo,
            text="Observação"
        ).pack(
            anchor="w",
            padx=10
        )
        
        txt_observacao = tk.Text(
            frame_conteudo,
            height=4
        )
        
        txt_observacao.pack(
            fill="x",
            padx=10,
            pady=5
        )

        tk.Button(
            frame_botoes_itens,
            text="Incluir Item",
            command=incluir_item
        ).pack(
            side="left",
            padx=5
        )
        
        tk.Button(
            frame_botoes_itens,
            text="Remover Item"
        ).pack(
            side="left",
            padx=5
        )
       

        tk.Button(
            frame_conteudo,
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

    
