import tkinter as tk

from database.database_service import DatabaseService

from views.frames.dashboard_frame import DashboardFrame
try:
    from views.frames.licitacoes_frame import LicitacoesFrame
except Exception as e:
    import traceback

    print("\nERRO REAL:\n")
    traceback.print_exc()

    input("\nPressione ENTER...")
    raise
from views.frames.movimentacoes_frame import MovimentacoesFrame
from views.frames.relatorios_frame import RelatoriosFrame
from views.frames.cadastros_frame import CadastrosFrame
from views.frames.entradas_frame import EntradasFrame
from views.frames.pacientes_frame import PacientesFrame
#from views.frames.solicitacoes_frame import SolicitacoesFrame


class MainView(tk.Tk):

    def __init__(self):
        super().__init__()

        DatabaseService.initialize_database()

        self.title("SIGOPME")
        self.geometry("1200x700")

        self.criar_layout()

        self.mostrar_dashboard()

    def criar_layout(self):

        titulo = tk.Label(
            self,
            text="SIGOPME",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=10)

        estilo_menu = {
            "width": 30,
            "height": 4,
            "font": ("Arial", 10, "bold")
        }

        barra_menu = tk.Frame(self)

        barra_menu.pack(
            fill="x",
            padx=20
        )

        tk.Button(
            barra_menu,
            text="Dashboard",
            command=self.mostrar_dashboard,
            **estilo_menu
        ).pack(side="left", padx=5)
        
        tk.Button(
            barra_menu,
            text="Cadastros",
            command=self.mostrar_cadastros,
            **estilo_menu
        ).pack(side="left", padx=5)
        
        tk.Button(
            barra_menu,
            text="Licitações",
            command=self.mostrar_licitacoes,
            **estilo_menu
        ).pack(side="left", padx=5)
        
        tk.Button(
            barra_menu,
            text="Entradas",
            command=self.mostrar_entradas,
            **estilo_menu
        ).pack(side="left", padx=5)

        """tk.Button(
            barra_menu,
            text="Solicitações",
            command=self.mostrar_solicitacoes
        ).pack(
            side="left",
            padx=5
        )"""
        
        tk.Button(
            barra_menu,
            text="Relatórios",
            command=self.mostrar_relatorios,
            **estilo_menu
        ).pack(side="left", padx=5)

        self.area_conteudo = tk.Frame(
            self
        )

        self.area_conteudo.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
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

        DashboardFrame(
            self.area_conteudo
        ).pack(
            fill="both",
            expand=True
        )

    def mostrar_licitacoes(self):

        self.limpar_area()

        LicitacoesFrame(
            self.area_conteudo
        ).pack(
            fill="both",
            expand=True
        )

    def mostrar_movimentacoes(self):

        self.limpar_area()

        MovimentacoesFrame(
            self.area_conteudo
        ).pack(
            fill="both",
            expand=True
        )

    def mostrar_relatorios(self):

        self.limpar_area()

        RelatoriosFrame(
            self.area_conteudo
        ).pack(
            fill="both",
            expand=True
        )

    def mostrar_cadastros(self):

        self.limpar_area()
    
        frame = CadastrosFrame(
            self.area_conteudo
        )
    
        frame.pack(
            fill="both",
            expand=True
        )

    def mostrar_entradas(self):

        self.limpar_area()
    
        EntradasFrame(
            self.area_conteudo
        ).pack(
            fill="both",
            expand=True
        )

    """def mostrar_solicitacoes(self):

        self.limpar_area()
    
        frame = SolicitacoesFrame(
            self.area_conteudo
        )
    
        frame.pack(
            fill="both",
            expand=True
        )"""
