import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.solicitacao_service import SolicitacaoService
from services.paciente_service import PacienteService
from services.historico_service import HistoricoService
from services.estoque_rastreado_service import (
    EstoqueRastreadoService
)
from services.nota_itens_service import (
    NotaItensService
)
from services.solicitacao_itens_service import (
    SolicitacaoItensService
)
from services.protocolo_rastreabilidade_service import (
    ProtocoloRastreabilidadeService
)

from views.components.masks import (
    aplicar_mascara_data,
    aplicar_mascara_moeda
)


class SolicitacoesFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.protocolo_service = (
            ProtocoloRastreabilidadeService()
        )

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

        frame_destino = tk.LabelFrame(
            self,
            text="Destino"
        )
        
        frame_destino.pack(
            fill="x",
            padx=10,
            pady=10
        )
        
        self.tipo_destino = tk.StringVar(
            value="PACIENTE"
        )

        tk.Radiobutton(
            frame_destino,
            text="Paciente",
            variable=self.tipo_destino,
            value="PACIENTE"
        ).pack(side="left", padx=5)
        
        tk.Radiobutton(
            frame_destino,
            text="Sala",
            variable=self.tipo_destino,
            value="SALA"
        ).pack(side="left", padx=5)

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
        
        aplicar_mascara_data(
            self.txt_data_retirada
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

        aplicar_mascara_data(
            self.txt_data_utilizacao
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

        aplicar_mascara_data(
            self.txt_data_devolucao
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
        
            "registro",
        
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
            "registro",
            text="Registro"
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

        self.grid_protocolos.bind(
            "<Double-1>",
            self.carregar_protocolo
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

        aplicar_mascara_data(
            self.txt_data_retirada_sala
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

        aplicar_mascara_data(
            self.txt_data_utilizacao_sala
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

        aplicar_mascara_data(
            self.txt_data_devolucao_sala
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
            command=self.registrar_sala
        )
        
        self.btn_registrar_sala.pack(
            side="left",
            padx=5
        )
        
        self.btn_utilizado_sala = tk.Button(
            frame_botoes_sala,
            text="Utilizado",
            #command=self.utilizado_sala
            state="disabled"
        )
        
        self.btn_utilizado_sala.pack(
            side="left",
            padx=5
        )
        
        self.btn_devolver_sala = tk.Button(
            frame_botoes_sala,
            text="Devolver",
            #command=self.devolver_sala
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

    def alterar_destino(self):

        if self.tipo_destino.get() == "PACIENTE":
    
            self.frame_paciente.select()
    
        else:
    
            self.frame_sala.select()

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
            self.localizar_por_registro
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
    
        resultado = NotaItensService.buscar_item(
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
    
            messagebox.showwarning(
                "SIGOPME",
                "Item não encontrado."
            )
    
            return
    
        if len(resultado) == 1:
    
            resultado = resultado[0]
    
        elif len(resultado) > 1:
    
            self.selecionar_item_encontrado(
                resultado
            )
    
            return
    
        (
            cod_item,
            nome_material,
            lote,
            serie_produto,
            data_validade,
            quantidade
        ) = resultado
    
        self.cod_item = cod_item
    
        self.nome_material = nome_material
    
        self.lote = lote
    
        self.serie_produto = serie_produto
    
        self.quantidade_disponivel = quantidade
    
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
            text=f"Série: {serie_produto}"
        )
    
        self.lbl_status.config(
            text=f"Qtd Disponível: {quantidade}"
        )
    
        self.lbl_codigo_barras.config(
            text=f"Validade: {data_validade}"
        )
    
        self.txt_paciente.delete(
            0,
            tk.END
        )
    
        self.txt_registro.delete(
            0,
            tk.END
        )
    
        self.txt_sala.delete(
            0,
            tk.END
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
    
        protocolo = (
            SolicitacaoService.buscar_protocolo_por_item(
                cod_item,
                lote
            )
        )
    
        if protocolo:
    
            self.protocolo_id = protocolo[0]
    
            self.txt_registro.insert(
                0,
                protocolo[1]
            )
    
            self.txt_paciente.insert(
                0,
                protocolo[2]
            )

    def selecionar_item_encontrado(
        self,
        resultado
    ):
    
        janela = tk.Toplevel(self)
    
        janela.title(
            "Selecionar Item"
        )
    
        janela.geometry(
            "1200x400"
        )
    
        colunas = (
    
            "codigo",
    
            "lote",
    
            "material",
    
            "validade",
    
            "quantidade"
    
        )
    
        grid = ttk.Treeview(
    
            janela,
    
            columns=colunas,
    
            show="headings"
    
        )
    
        grid.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )
    
        grid.heading(
            "codigo",
            text="Código"
        )
    
        grid.heading(
            "lote",
            text="Lote"
        )
    
        grid.heading(
            "material",
            text="Material"
        )
    
        grid.heading(
            "validade",
            text="Validade"
        )
    
        grid.heading(
            "quantidade",
            text="Qtd"
        )
    
        grid.column(
            "codigo",
            width=100
        )
    
        grid.column(
            "lote",
            width=180
        )
    
        grid.column(
            "material",
            width=600
        )
    
        grid.column(
            "validade",
            width=120
        )
    
        grid.column(
            "quantidade",
            width=80
        )
    
        for item in resultado:
    
            grid.insert(
                "",
                "end",
                values=(
    
                    item[0],  # código
                    item[2],  # lote
                    item[1],  # material
                    item[4],  # validade
                    item[5]   # quantidade
    
                )
            )
    
        def selecionar(event=None):
    
            selecionado = grid.selection()
    
            if not selecionado:
                return
    
            valores = grid.item(
                selecionado[0]
            )["values"]
    
            (
                cod_item,
                lote,
                nome_material,
                data_validade,
                quantidade
            ) = valores
    
            self.cod_item = cod_item
    
            self.nome_material = nome_material
    
            self.lote = lote
    
            self.quantidade_disponivel = quantidade
    
            self.lbl_cod_item.config(
                text=f"Cód Item: {cod_item}"
            )
    
            self.lbl_material.config(
                text=f"Nome Material: {nome_material}"
            )
    
            self.lbl_lote.config(
                text=f"Lote: {lote}"
            )
    
            self.lbl_status.config(
                text=f"Qtd Disponível: {quantidade}"
            )
    
            self.lbl_codigo_barras.config(
                text=f"Validade: {data_validade}"
            )
    
            protocolo = (
                SolicitacaoService.buscar_protocolo_por_item(
                    cod_item,
                    lote
                )
            )
    
            self.txt_paciente.delete(
                0,
                tk.END
            )
    
            self.txt_registro.delete(
                0,
                tk.END
            )
    
            if protocolo:
    
                self.protocolo_id = protocolo[0]
    
                self.txt_registro.insert(
                    0,
                    protocolo[1]
                )
    
                self.txt_paciente.insert(
                    0,
                    protocolo[2]
                )
    
            janela.destroy()
    
        grid.bind(
            "<Double-1>",
            selecionar
        )

    def limpar_tela(self):

        self.txt_busca.delete(
            0,
            tk.END
        )
    
        self.txt_paciente.delete(
            0,
            tk.END
        )
    
        self.txt_registro.delete(
            0,
            tk.END
        )
    
        self.txt_sala.delete(
            0,
            tk.END
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
    
        self.lbl_licitacao.config(
            text="Licitação:"
        )
    
        self.lbl_status.config(
            text="Status:"
        )
    
        self.lbl_cod_item.config(
            text="Cod Item:"
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
    
        self.protocolo_id = None
    
        if hasattr(self, "cod_item"):
            del self.cod_item

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

    def carregar_protocolo(self, event=None):

        selecionado = self.grid_protocolos.selection()
    
        if not selecionado:
            return
    
        valores = self.grid_protocolos.item(
            selecionado[0]
        )["values"]
    
        protocolo = valores[0]
    
        dados = self.protocolo_service.obter_protocolo_completo(
            protocolo
        )
        print("Data retirada:", dados.data_retirada)
    
        if not dados:
            return
    
        self.protocolo_id = protocolo
    
        self.preencher_protocolo(dados)

    def preencher_protocolo(self, dados):

        # Paciente
        self.txt_registro.delete(0, tk.END)
        self.txt_registro.insert(0, dados.registro)
    
        self.txt_paciente.delete(0, tk.END)
        self.txt_paciente.insert(0, dados.paciente)
    
        # Datas
        self.txt_data_retirada.delete(0, tk.END)
        self.txt_data_retirada.insert(
            0,
            dados.data_retirada or ""
        )
    
        self.txt_data_utilizacao.delete(0, tk.END)
        self.txt_data_utilizacao.insert(
            0,
            dados.data_utilizacao or ""
            if dados.data_utilizacao else ""
        )
    
        self.txt_data_devolucao.delete(0, tk.END)
        self.txt_data_devolucao.insert(
            0,
            dados.data_devolucao or ""
            if dados.data_devolucao else ""
        )
    
        # Dados do Item
        self.lbl_licitacao.config(
            text=f"Licitação: {dados.licitacao}"
        )
    
        self.lbl_status.config(
            text=f"Status: {dados.status}"
        )
    
        self.lbl_cod_item.config(
            text=f"Cod Item: {dados.codigo_item}"
        )
    
        self.lbl_material.config(
            text=f"Nome Material: {dados.nome_material}"
        )
    
        self.lbl_lote.config(
            text=f"Lote: {dados.lote}"
        )
    
        self.lbl_serie.config(
            text=f"Série: {dados.serie}"
        )
    
        self.lbl_codigo_barras.config(
            text=f"Código Barras: {dados.codigo_barras}"
        )

    def atualizar_protocolo(self):

        registro = self.txt_registro.get().strip()
    
        nome = self.txt_paciente.get().strip()
    
        sala = self.txt_sala.get().strip()
    
        data_retirada = (
            self.txt_data_retirada.get().strip()
        )
    
        if self.tipo_destino.get() == "PACIENTE":
    
            sala = ""
    
        else:
    
            registro = ""
            nome = ""
    
        self.protocolo_service.atualizar_protocolo(
    
            self.protocolo_id,
    
            registro,
    
            nome,
    
            sala,
    
            data_retirada
    
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Protocolo atualizado com sucesso."
        )
    
        self.carregar_protocolos()
    
        self.protocolo_id = None
    
        self.limpar_tela()
        
    def registrar(self):

        if self.protocolo_id:
            self.atualizar_protocolo()
            return
    
        if self.tipo_destino.get() == "PACIENTE":

            self.registrar_novo_protocolo()
        
        else:
        
            self.registrar_sala()


    def registrar_novo_protocolo(self):

        if not hasattr(self, "cod_item"):
    
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
    
        numero_protocolo = (
            f"PROTO-{registro}"
        )
    
        solicitacao_id = (
            SolicitacaoService.inserir(

                numero_protocolo,
            
                data,
            
                "",
            
                registro,
            
                nome,
            
                "",
            
                f"Entrega do item {self.cod_item}",
            
                "SIGOPME"
            
            )
        )
    
        SolicitacaoItensService.inserir(

            solicitacao_id,
        
            self.cod_item,
        
            self.nome_material,
        
            self.lote,
        
            1
        
        )
    
        HistoricoService.registrar(
    
            tipo="SOLICITACAO",
    
            acao="ITEM_RETIRADO",
    
            paciente_nome=nome,
    
            paciente_registro=registro,
    
            cod_item=self.cod_item,
    
            nome_material=self.nome_material,
    
            lote=self.lote,
    
            observacao="Material entregue ao paciente"
    
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Solicitação registrada."
        )
    
        self.carregar_protocolos()
        
    def utilizado(self):

        selecionado = (
            self.grid_protocolos.selection()
        )
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione um protocolo."
            )
    
            return
    
        data = (
            self.txt_data_utilizacao.get().strip()
        )
    
        if not data:
    
            messagebox.showwarning(
                "SIGOPME",
                "Informe a data de utilização."
            )
    
            return
    
        protocolo = self.grid_protocolos.item(
            selecionado[0]
        )["values"][0]
    
        item = (
            SolicitacaoItensService.obter_por_protocolo(
                protocolo
            )
        )
    
        if not item:
            return
    
        item_id = item[0]

        print("SolicitacaoItens.Id =", item_id)

        SolicitacaoService.utilizado(
            item_id,
            data
        )
    
        SolicitacaoItensService.registrar_utilizacao(
            item_id,
            data
        )
    
        HistoricoService.registrar(
    
            tipo="SOLICITACAO",
    
            acao="ITEM_UTILIZADO",
    
            referencia_id=item_id
    
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Material marcado como utilizado."
        )
    
        self.carregar_protocolos()

    def devolver(self):

        selecionado = (
            self.grid_protocolos.selection()
        )
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione um protocolo."
            )
    
            return
    
        data = (
            self.txt_data_devolucao.get().strip()
        )
    
        if not data:
    
            messagebox.showwarning(
                "SIGOPME",
                "Informe a data de devolução."
            )
    
            return
    
        protocolo = self.grid_protocolos.item(
            selecionado[0]
        )["values"][0]
    
        item = (
            SolicitacaoItensService.obter_por_protocolo(
                protocolo
            )
        )
    
        if not item:
            return
    
        item_id = item[0]

        print("SolicitacaoItens.Id =", item_id)

        SolicitacaoService.devolver(
            item_id,
            data
        )
        
        SolicitacaoItensService.registrar_devolucao(
            item_id,
            data
        )
        
        HistoricoService.registrar(
    
            tipo="SOLICITACAO",
    
            acao="ITEM_DEVOLVIDO",
    
            referencia_id=item_id
    
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Material devolvido."
        )
    
        self.carregar_protocolos()


    def registrar_sala(self):

        if not hasattr(self, "cod_item"):
    
            messagebox.showwarning(
                "SIGOPME",
                "Pesquise um item primeiro."
            )
    
            return
    
        sala = self.txt_sala.get().strip()
    
        data = (
            self.txt_data_retirada_sala.get().strip()
        )
    
        if not sala:
    
            messagebox.showwarning(
                "SIGOPME",
                "Informe a sala."
            )
    
            return
    
        numero_protocolo = (
            f"SALA-{sala}"
        )
    
        solicitacao_id = (
            SolicitacaoService.inserir(
    
                numero_protocolo,
                data,
    
                "",
    
                "",      # registro
                "",      # paciente
                sala,    # sala
    
                "",
    
                f"Entrega do item {self.cod_item}",
    
                "SIGOPME"
    
            )
        )
    
        SolicitacaoItensService.inserir(
    
            solicitacao_id,
    
            self.cod_item,
    
            self.nome_material,
    
            self.lote,
    
            1
    
        )
    
        HistoricoService.registrar(
    
            tipo="SOLICITACAO",
    
            acao="ITEM_SALA",
    
            cod_item=self.cod_item,
    
            nome_material=self.nome_material,
    
            lote=self.lote,
    
            observacao=f"Material entregue para sala {sala}"
    
        )
    
        messagebox.showinfo(
            "SIGOPME",
            "Solicitação registrada."
        )
    
        self.carregar_protocolos()
    
        self.limpar_tela()
    
