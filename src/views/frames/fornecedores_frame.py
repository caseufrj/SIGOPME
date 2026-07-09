import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from services.fornecedor_service import FornecedorService
from views.components.grid_helper import criar_treeview
from views.components.search_helper import criar_barra_pesquisa

class FornecedoresFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()
        self.carregar_dados()

    def criar_componentes(self):

        titulo = tk.Label(
            self,
            text="Fornecedores",
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

        frame_pesquisa, self.txt_pesquisa = criar_barra_pesquisa(
            barra,
            self.pesquisar
        )

        tk.Button(
            barra,
            text="Novo",
            command=self.novo
        ).pack(
            side="left",
            padx=5
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
        frame_pesquisa, self.txt_pesquisa = criar_barra_pesquisa(
            barra
        )
        
        frame_pesquisa.pack(
            side="right"
        )

        colunas = (
            "id",
            "nome",
            "cnpj",
            "telefone",
            "contato",
            "email"
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
            "nome",
            text="Nome"
        )

        self.grid.heading(
            "cnpj",
            text="CNPJ"
        )

        self.grid.heading(
            "telefone",
            text="Telefone"
        )

        self.grid.heading(
            "contato",
            text="Contato"
        )

        self.grid.heading(
            "email",
            text="Email"
        )

        self.grid.column(
            "id",
            width=0,
            stretch=False
        )

        self.grid.column(
            "nome",
            width=300
        )

        self.grid.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def carregar_dados(self):

        for item in self.grid.get_children():
            self.grid.delete(item)

        dados = FornecedorService.listar_todos()

        for fornecedor in dados:

            self.grid.insert(
                "",
                "end",
                values=fornecedor
            )

    def novo(self):

        janela = tk.Toplevel(self)

        janela.title(
            "Novo Fornecedor"
        )

        janela.geometry(
            "500x350"
        )

        tk.Label(
            janela,
            text="Nome"
        ).pack()

        txt_nome = tk.Entry(
            janela
        )

        txt_nome.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="CNPJ"
        ).pack()

        txt_cnpj = tk.Entry(
            janela
        )

        txt_cnpj.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Telefone"
        ).pack()

        txt_telefone = tk.Entry(
            janela
        )

        txt_telefone.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Contato"
        ).pack()

        txt_contato = tk.Entry(
            janela
        )

        txt_contato.pack(
            fill="x",
            padx=10
        )

        tk.Label(
            janela,
            text="Email"
        ).pack()

        txt_email = tk.Entry(
            janela
        )

        txt_email.pack(
            fill="x",
            padx=10
        )

        def salvar():

            FornecedorService.inserir(
                txt_nome.get(),
                txt_cnpj.get(),
                txt_telefone.get(),
                txt_contato.get(),
                txt_email.get()
            )

            self.carregar_dados()

            janela.destroy()

        tk.Button(
            janela,
            text="Salvar",
            command=salvar
        ).pack(
            pady=10
        )

    def excluir(self):

        selecionado = self.grid.selection()

        if not selecionado:

            messagebox.showwarning(
                "SIGOPME",
                "Selecione um fornecedor."
            )

            return

        item = self.grid.item(
            selecionado[0]
        )

        id_registro = item["values"][0]

        confirmar = messagebox.askyesno(
            "SIGOPME",
            "Deseja excluir este fornecedor?"
        )

        if not confirmar:
            return

        FornecedorService.excluir(
            id_registro
        )

        self.carregar_dados()

    def editar(self):
    
        selecionado = self.grid.selection()
    
        if not selecionado:
    
            messagebox.showwarning(
                "SIGOPME",
                "Selecione um fornecedor."
            )
    
            return
    
        item = self.grid.item(
            selecionado[0]
        )
    
        id_registro = item["values"][0]
    
        dados = FornecedorService.obter_por_id(
            id_registro
        )
    
        if not dados:
            return
    
        (
            _id,
            nome,
            cnpj,
            telefone,
            contato,
            email
        ) = dados
    
        janela = tk.Toplevel(self)
    
        janela.title(
            "Editar Fornecedor"
        )
    
        janela.geometry(
            "500x350"
        )
    
        tk.Label(
            janela,
            text="Nome"
        ).pack()
    
        txt_nome = tk.Entry(janela)
    
        txt_nome.pack(
            fill="x",
            padx=10
        )
    
        txt_nome.insert(
            0,
            nome or ""
        )
    
        tk.Label(
            janela,
            text="CNPJ"
        ).pack()
    
        txt_cnpj = tk.Entry(janela)
    
        txt_cnpj.pack(
            fill="x",
            padx=10
        )
    
        txt_cnpj.insert(
            0,
            cnpj or ""
        )
    
        tk.Label(
            janela,
            text="Telefone"
        ).pack()
    
        txt_telefone = tk.Entry(janela)
    
        txt_telefone.pack(
            fill="x",
            padx=10
        )
    
        txt_telefone.insert(
            0,
            telefone or ""
        )
    
        tk.Label(
            janela,
            text="Contato"
        ).pack()
    
        txt_contato = tk.Entry(janela)
    
        txt_contato.pack(
            fill="x",
            padx=10
        )
    
        txt_contato.insert(
            0,
            contato or ""
        )
    
        tk.Label(
            janela,
            text="Email"
        ).pack()
    
        txt_email = tk.Entry(janela)
    
        txt_email.pack(
            fill="x",
            padx=10
        )
    
        txt_email.insert(
            0,
            email or ""
        )
    
        def salvar():
    
            FornecedorService.atualizar(
                id_registro,
                txt_nome.get(),
                txt_cnpj.get(),
                txt_telefone.get(),
                txt_contato.get(),
                txt_email.get()
            )
    
            self.carregar_dados()
    
            janela.destroy()
    
            messagebox.showinfo(
                "SIGOPME",
                "Fornecedor atualizado."
            )
    
        tk.Button(
            janela,
            text="Salvar Alterações",
            command=salvar
        ).pack(
            pady=10
        )

    def pesquisar(self, event=None):

        texto = self.txt_pesquisa.get()
    
        for item in self.grid.get_children():
            self.grid.delete(item)
    
        dados = FornecedorService.pesquisar(
            texto
        )
    
        for fornecedor in dados:
    
            self.grid.insert(
                "",
                "end",
                values=fornecedor
            )
