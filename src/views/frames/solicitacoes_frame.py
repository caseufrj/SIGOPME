import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.solicitacao_service import SolicitacaoService
from services.paciente_service import PacienteService
from services.historico_service import HistoricoService
from services.estoque_rastreado_service import (
    EstoqueRastreadoService
)

class SolicitacoesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()

        self.carregar_protocolos()

    def criar_componentes(self):

        titulo = tk.Label(
            self,
            text="Solicitações / Rastreabilidade",
            font=("Arial", 18, "bold")
        )

        titulo.pack(
            pady=10
        )

        frame_busca = tk.Frame(self)

        frame_busca.pack(
            fill="x",
            padx=10,
            pady=10
        )

        tk.Label(
            frame_busca,
            text="Código de Barras / Lote / Série / Código Item"
        ).pack(
            anchor="w"
        )

        self.txt_busca = tk.Entry(
            frame_busca
        )

        self.txt_busca.pack(
            side="left",
            fill="x",
            expand=True
        )

        tk.Button(
            frame_busca,
            text="Pesquisar",
            command=self.pesquisar
        ).pack(
            side="left",
            padx=5
        )

        frame_item = tk.LabelFrame(
            self,
            text="Dados do Item"
        )
        
        frame_item.pack(
            fill="x",
            padx=10,
            pady=10
        )

        notebook = ttk.Notebook(self)

        notebook.pack(
            fill="x",
            padx=10,
            pady=10
        )
        
        self.frame_paciente = tk.Frame(notebook)
        self.frame_sala = tk.Frame(notebook)
        
        notebook.add(
            self.frame_paciente,
            text="Paciente"
        )
        
        notebook.add(
            self.frame_sala,
            text="Sala"
        )

        #====================
        # ABA PACIENTE
        #====================
        tk.Label(
            self.frame_paciente,
            text="Paciente"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        
        self.txt_paciente = tk.Entry(
            self.frame_paciente,
            width=50
        )
        
        self.txt_paciente.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )
        self.txt_paciente.bind(
            "<FocusOut>",
            self.localizar_por_nome
        )

        tk.Label(
            self.frame_paciente,
            text="Registro"
        ).grid(
            row=0,
            column=2,
            sticky="w",
            padx=5,
            pady=5
        )
        
        self.txt_registro = tk.Entry(
            self.frame_paciente,
            width=20
        )
        
        self.txt_registro.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )
        self.txt_registro.bind(
            "<FocusOut>",
            self.localizar_por_registro
        )
        

        tk.Label(
            self.frame_paciente,
            text="Data Retirada"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        
        self.txt_data_retirada = tk.Entry(
            self.frame_paciente,
            width=15
        )
        
        self.txt_data_retirada.grid(
            row=1,
            column=1,
            sticky="w"
        )

        tk.Label(
            self.frame_paciente,
            text="Data Utilização"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        
        self.txt_data_utilizacao = tk.Entry(
            self.frame_paciente,
            width=15
        )
        
        self.txt_data_utilizacao.grid(
            row=2,
            column=1,
            sticky="w"
        )

        tk.Label(
            self.frame_paciente,
            text="Data Devolução"
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        
        self.txt_data_devolucao = tk.Entry(
            self.frame_paciente,
            width=15
        )
        
        self.txt_data_devolucao.grid(
            row=3,
            column=1,
            sticky="w"
        )

        frame_botoes = tk.Frame(
            self.frame_paciente
        )
        
        frame_botoes.grid(
            row=4,
            column=0,
            columnspan=4,
            pady=10
        )

        self.btn_registrar = tk.Button(
            frame_botoes,
            text="Registrar",
            command=self.registrar
        )

        self.btn_registrar.pack(
            side="left",
            padx=5
        )

        self.btn_utilizado = tk.Button(
            frame_botoes,
            text="Utilizado",
            command=self.utilizado
        )
        
        self.btn_utilizado.pack(
            side="left",
            padx=5
        )

        self.btn_devolver = tk.Button(
            frame_botoes,
            text="Devolver",
            command=self.devolver
        )
        
        self.btn_devolver.pack(
            side="left",
            padx=5
        )

        frame_protocolos = tk.LabelFrame(
            self,
            text="Protocolos em Aberto"
        )
        
        frame_protocolos.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        colunas = (

            "protocolo",
        
            "paciente_sala",
        
            "material",
        
            "lote",
        
            "status"
        
        )

        self.grid_protocolos = ttk.Treeview(

            frame_protocolos,
        
            columns=colunas,
        
            show="headings"
        
        )
        
        self.grid_protocolos.pack(
            fill="both",
            expand=True
        )

        self.grid_protocolos.heading(
            "protocolo",
            text="Protocolo"
        )
        
        self.grid_protocolos.heading(
            "paciente_sala",
            text="Paciente / Sala"
        )
        
        self.grid_protocolos.heading(
            "material",
            text="Material"
        )
        
        self.grid_protocolos.heading(
            "lote",
            text="Lote"
        )
        
        self.grid_protocolos.heading(
            "status",
            text="Status"
        )

        self.grid_protocolos.column(
            "protocolo",
            width=100
        )
        
        self.grid_protocolos.column(
            "paciente_sala",
            width=250
        )
        
        self.grid_protocolos.column(
            "material",
            width=450
        )
        
        self.grid_protocolos.column(
            "lote",
            width=120
        )
        
        self.grid_protocolos.column(
            "status",
            width=120
        )

        # ====================
        # ABA SALA
        # ====================
        
        tk.Label(
            self.frame_sala,
            text="Sala"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            padx=5,
            pady=5
        )
        
        self.txt_sala = tk.Entry(
            self.frame_sala,
            width=50
        )
        
        self.txt_sala.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            self.frame_sala,
            text="Data Retirada"
        ).grid(
            row=1,
            column=0,
            sticky="w"
        )
        
        self.txt_data_retirada_sala = tk.Entry(
            self.frame_sala,
            width=15
        )
        
        self.txt_data_retirada_sala.grid(
            row=1,
            column=1,
            sticky="w"
        )

        tk.Label(
            self.frame_sala,
            text="Data Utilização"
        ).grid(
            row=2,
            column=0,
            sticky="w"
        )
        
        self.txt_data_utilizacao_sala = tk.Entry(
            self.frame_sala,
            width=15
        )
        
        self.txt_data_utilizacao_sala.grid(
            row=2,
            column=1,
            sticky="w"
        )

        tk.Label(
            self.frame_sala,
            text="Data Devolução"
        ).grid(
            row=3,
            column=0,
            sticky="w"
        )
        
        self.txt_data_devolucao_sala = tk.Entry(
            self.frame_sala,
            width=15
        )
        
        self.txt_data_devolucao_sala.grid(
            row=3,
            column=1,
            sticky="w"
        )

        frame_botoes_sala = tk.Frame(
            self.frame_sala
        )
        
        frame_botoes_sala.grid(
            row=4,
            column=0,
            columnspan=4,
            pady=10
        )

        self.btn_registrar_sala = tk.Button(
            frame_botoes_sala,
            text="Registrar",
            state="disabled"
        )
        
        self.btn_registrar_sala.pack(
            side="left",
            padx=5
        )
        
        self.btn_utilizado_sala = tk.Button(
            frame_botoes_sala,
            text="Utilizado",
            state="disabled"
        )
        
        self.btn_utilizado_sala.pack(
            side="left",
            padx=5
        )
        
        self.btn_devolver_sala = tk.Button(
            frame_botoes_sala,
            text="Devolver",
            state="disabled"
        )
        
        self.btn_devolver_sala.pack(
            side="left",
            padx=5
        )
        
        # Linha 1
        
        self.lbl_licitacao = tk.Label(
            frame_item,
            text="Licitação:"
        )
        
        self.lbl_licitacao.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )
        
        self.lbl_status = tk.Label(
            frame_item,
            text="Status:"
        )
        
        self.lbl_status.grid(
            row=0,
            column=1,
            padx=20,
            pady=5,
            sticky="w"
        )
        
        # Linha 2
        
        self.lbl_cod_item = tk.Label(
            frame_item,
            text="Cod Item:"
        )
        
        self.lbl_cod_item.grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )
        
        self.lbl_material = tk.Label(
            frame_item,
            text="Nome Material:"
        )
        
        self.lbl_material.grid(
            row=1,
            column=1,
            padx=20,
            pady=5,
            sticky="w"
        )
        
        # Linha 3
        
        self.lbl_lote = tk.Label(
            frame_item,
            text="Lote:"
        )
        
        self.lbl_lote.grid(
            row=2,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )
        
        self.lbl_serie = tk.Label(
            frame_item,
            text="Série:"
        )
        
        self.lbl_serie.grid(
            row=2,
            column=1,
            padx=20,
            pady=5,
            sticky="w"
        )
        
        # Linha 4
        
        self.lbl_codigo_barras = tk.Label(
            frame_item,
            text="Código Barras:"
        )
        
        self.lbl_codigo_barras.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="w"
        )

    def localizar_por_registro(self, event=None):

        registro = self.txt_registro.get().strip()
    
        if not registro:
            return
    
        paciente = (
            PacienteService.obter_por_registro(
                registro
            )
        )
    
        if not paciente:
            return
    
        self.txt_paciente.delete(
            0,
            tk.END
        )
    
        self.txt_paciente.insert(
            0,
            paciente[2]
        )
        self.txt_registro.bind(
            "<FocusOut>",
            localizar_por_registro
        )

    def localizar_por_nome(self, event=None):

        nome = self.txt_paciente.get().strip()
    
        if not nome:
            return
    
        paciente = (
            PacienteService.obter_por_nome(
                nome
            )
        )
    
        if not paciente:
            return
    
        self.txt_registro.delete(
            0,
            tk.END
        )
    
        self.txt_registro.insert(
            0,
            paciente[1]
        )
        

    def pesquisar(self):

        texto = self.txt_busca.get().strip()
    
        if not texto:
    
            messagebox.showwarning(
                "SIGOPME",
                "Informe um valor para pesquisa."
            )
    
            return
    
        resultado = SolicitacaoService.buscar_item(
            texto
        )
    
        if not resultado:
    
            self.lbl_licitacao.config(
                text="Licitação:"
            )
    
            self.lbl_status.config(
                text="Status:"
            )
    
            self.lbl_cod_item.config(
                text="Cód Item:"
            )
    
            self.lbl_material.config(
                text="Nome Material:"
            )
    
            self.lbl_lote.config(
                text="Lote:"
            )
    
            self.lbl_serie.config(
                text="Série:"
            )
    
            self.lbl_codigo_barras.config(
                text="Código Barras:"
            )
    
            return
    
        (
            _id,
            licitacao_item_id,
            numero_licitacao,
            cod_item,
            nome_material,
            lote,
            codigo_unico,
            codigo_barras,
            quantidade,
            status,
            paciente_id,
            paciente_registro,
            paciente_nome,
            sala,
            data_entrada,
            data_retirada,
            data_utilizacao,
            data_devolucao,
            data_extravio,
            data_pagamento,
            observacao
        ) = resultado

        self.id_item = _id
    
        self.lbl_licitacao.config(
            text=f"Licitação: {numero_licitacao}"
        )
        
        self.lbl_status.config(
            text=f"Status: {status}"
        )
        
        self.lbl_cod_item.config(
            text=f"Cód Item: {cod_item}"
        )
        
        self.lbl_material.config(
            text=f"Nome Material: {nome_material}"
        )
        
        self.lbl_lote.config(
            text=f"Lote: {lote}"
        )
        
        self.lbl_serie.config(
            text=f"Série: {codigo_unico}"
        )
        
        self.lbl_codigo_barras.config(
            text=f"Código Barras: {codigo_barras}"
        )

        self.txt_paciente.delete(0, tk.END)
        self.txt_registro.delete(0, tk.END)
        self.txt_sala.delete(0, tk.END)
        
        if paciente_nome:
            self.txt_paciente.insert(
                0,
                paciente_nome
            )
        
        if paciente_registro:
            self.txt_registro.insert(
                0,
                paciente_registro
            )
        
        if sala:
            self.txt_sala.insert(
                0,
                sala
            )

        self.txt_data_retirada.delete(
            0,
            tk.END
        )
        
        self.txt_data_utilizacao.delete(
            0,
            tk.END
        )
        
        self.txt_data_devolucao.delete(
            0,
            tk.END
        )
        
        if data_retirada:
        
            self.txt_data_retirada.insert(
                0,
                data_retirada
            )
        
        if data_utilizacao:
        
            self.txt_data_utilizacao.insert(
                0,
                data_utilizacao
            )
        
        if data_devolucao:
        
            self.txt_data_devolucao.insert(
                0,
                data_devolucao
            )
        
        # =====================
        # PACIENTE / SALA
        # =====================
        
        self.txt_paciente.delete(0, tk.END)
        self.txt_registro.delete(0, tk.END)
        self.txt_sala.delete(0, tk.END)
        
        if paciente_nome:
        
            self.txt_paciente.insert(
                0,
                paciente_nome
            )
        
        if paciente_registro:
        
            self.txt_registro.insert(
                0,
                paciente_registro
            )
        
        if sala:
        
            self.txt_sala.insert(
                0,
                sala
            )

    def carregar_protocolos(self):

        for item in self.grid_protocolos.get_children():
    
            self.grid_protocolos.delete(item)
    
        dados = (
            SolicitacaoService.listar_protocolos_abertos()
        )
    
        for registro in dados:
    
            self.grid_protocolos.insert(
                "",
                "end",
                values=registro
            )

    def registrar(self):

        if not hasattr(self, "id_item"):
    
            messagebox.showwarning(
                "SIGOPME",
                "Pesquise um item primeiro."
            )
    
            return
    
        registro = (
            self.txt_registro.get().strip()
        )
    
        nome = (
            self.txt_paciente.get().strip()
        )
    
        data = (
            self.txt_data_retirada.get().strip()
        )
    
        if not registro or not nome:
    
            messagebox.showwarning(
                "SIGOPME",
                "Informe paciente e registro."
            )
    
            return
    
        paciente = (
            PacienteService.obter_por_registro(
                registro
            )
        )
    
        if not paciente:
    
            PacienteService.inserir(
                registro,
                nome
            )

        HistoricoService.registrar(

            tipo="PACIENTE",
        
            acao="PACIENTE_CADASTRADO",
        
            paciente_nome=nome,
        
            paciente_registro=registro
        
        )
    
        EstoqueRastreadoService.registrar_retirada(
    
            self.id_item,
    
            nome,
    
            registro,
    
            data
    
        )

        HistoricoService.registrar(

            tipo="MATERIAL",
        
            acao="ITEM_RETIRADO",
        
            referencia_id=self.id_item,
        
            paciente_nome=nome,
        
            paciente_registro=registro,
        
            observacao="Retirada para paciente"
        
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Retirada registrada."
        )
    
        self.pesquisar()

        self.carregar_protocolos()

        self.txt_data_utilizacao.delete(
            0,
            tk.END
        )
        
        self.txt_data_devolucao.delete(
            0,
            tk.END
        )
        
    def utilizado(self):

        data = self.txt_data_utilizacao.get().strip()
    
        if not data:
    
            messagebox.showwarning(
                "SIGOPME",
                "Informe a data de utilização."
            )
    
            return
    
        EstoqueRastreadoService.utilizado(
            self.id_item,
            data
        )

        HistoricoService.registrar(

            tipo="MATERIAL",
        
            acao="ITEM_UTILIZADO",
        
            referencia_id=self.id_item
        
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Material marcado como utilizado."
        )
    
        self.pesquisar()

        self.carregar_protocolos()

    def devolver(self):

        data = self.txt_data_devolucao.get().strip()
    
        if not data:
    
            messagebox.showwarning(
                "SIGOPME",
                "Informe a data de devolução."
            )
    
            return
    
        EstoqueRastreadoService.devolver(
            self.id_item,
            data
        )

        HistoricoService.registrar(

            tipo="MATERIAL",
        
            acao="ITEM_DEVOLVIDO",
        
            referencia_id=self.id_item
        
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Material devolvido."
        )
    
        self.pesquisar()

        self.carregar_protocolos()

    
