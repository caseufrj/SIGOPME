import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.solicitacao_service import SolicitacaoService

class SolicitacoesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()

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
            state="disabled"
        )
        
        self.btn_registrar.pack(
            side="left",
            padx=5
        )

        self.btn_utilizado = tk.Button(
            frame_botoes,
            text="Utilizado",
            state="disabled"
        )
        
        self.btn_utilizado.pack(
            side="left",
            padx=5
        )

        self.btn_devolver = tk.Button(
            frame_botoes,
            text="Devolver",
            state="disabled"
        )
        
        self.btn_devolver.pack(
            side="left",
            padx=5
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
            *resto
        ) = resultado
    
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
