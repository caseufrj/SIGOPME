import tkinter as tk
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
