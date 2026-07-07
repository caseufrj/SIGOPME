import tkinter as tk

from database.database_service import DatabaseService


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
            label="Licitações"
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
