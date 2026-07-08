import tkinter as tk

from database.database_service import DatabaseService

from views.frames.dashboard_frame import DashboardFrame
from views.frames.licitacoes_frame import LicitacoesFrame
from views.frames.movimentacoes_frame import MovimentacoesFrame
from views.frames.relatorios_frame import RelatoriosFrame


class MainView(tk.Tk):

    def __init__(self):
        super().__init__()

        DatabaseService.initialize_database()

        self.title("SIGOPME")
        self.geometry("1200x700")

        self.criar_layout()

        self.mostrar_dashboard()

    def criar_layout(self):

        self.menu_lateral = tk.Frame(
            self,
            width=200,
            bg="#EAEAEA"
        )

        self.menu_lateral.pack(
            side="left",
            fill="y"
        )

        self.menu_lateral.pack_propagate(False)

        titulo = tk.Label(
            self.menu_lateral,
            text="SIGOPME",
            bg="#EAEAEA",
            font=("Arial", 14, "bold")
        )

        titulo.pack(
            pady=20
        )

        btn_dashboard = tk.Button(
            self.menu_lateral,
            text="Dashboard",
            command=self.mostrar_dashboard
        )

        btn_dashboard.pack(
            fill="x",
            padx=10,
            pady=5
        )

        btn_licitacoes = tk.Button(
            self.menu_lateral,
            text="Licitações",
            command=self.mostrar_licitacoes
        )

        btn_licitacoes.pack(
            fill="x",
            padx=10,
            pady=5
        )

        btn_movimentacoes = tk.Button(
            self.menu_lateral,
            text="Movimentações",
            command=self.mostrar_movimentacoes
        )

        btn_movimentacoes.pack(
            fill="x",
            padx=10,
            pady=5
        )

        btn_relatorios = tk.Button(
            self.menu_lateral,
            text="Relatórios",
            command=self.mostrar_relatorios
        )

        btn_relatorios.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.area_conteudo = tk.Frame(
            self,
            bg="white"
        )

        self.area_conteudo.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.status_bar = tk.Label(
            self,
            text="SIGOPME v0.1",
            anchor="w"
        )

        self.status_bar.pack(
            side="bottom",
            fill="x"
        )

    def limpar_area(self):

        for widget in self.area_conteudo.winfo_children():
            widget.destroy()

    def mostrar_dashboard(self):

        self.limpar_area()

        frame = DashboardFrame(
            self.area_conteudo
        )

        frame.pack(
            fill="both",
            expand=True
        )

    def mostrar_licitacoes(self):

        self.limpar_area()

        frame = LicitacoesFrame(
            self.area_conteudo
        )

        frame.pack(
            fill="both",
            expand=True
        )

    def mostrar_movimentacoes(self):

        self.limpar_area()

        frame = MovimentacoesFrame(
            self.area_conteudo
        )

        frame.pack(
            fill="both",
            expand=True
        )

    def mostrar_relatorios(self):

        self.limpar_area()

        frame = RelatoriosFrame(
            self.area_conteudo
        )

        frame.pack(
            fill="both",
            expand=True
        )
