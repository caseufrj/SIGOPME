import tkinter as tk

from database.database_service import DatabaseService
from views.licitacoes_view import LicitacoesView


class MainView(tk.Tk):

    def __init__(self):
        super().__init__()

        DatabaseService.initialize_database()

        self.title("SIGOPME")
        self.geometry("1200x700")

        self.create_menu()

        titulo = tk.Label(
            self,
            text="SIGOPME",
            font=("Arial", 24, "bold")
        )

        titulo.pack(pady=20)

    def create_menu(self):

        menu_bar = tk.Menu(self)

        cadastro_menu = tk.Menu(
            menu_bar,
            tearoff=0
        )

        cadastro_menu.add_command(
            label="Licitações",
            command=self.abrir_licitacoes
        )

        cadastro_menu.add_command(
            label="Notas Fiscais"
        )

        cadastro_menu.add_command(
            label="Solicitações"
        )

        menu_bar.add_cascade(
            label="Cadastros",
            menu=cadastro_menu
        )

        self.config(menu=menu_bar)


    def abrir_licitacoes(self):
        LicitacoesView(self)
