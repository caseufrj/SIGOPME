import tkinter as tk
from tkinter import ttk

from services.entrada_service import EntradaService
from views.components.grid_helper import criar_treeview
from views.components.search_helper import criar_barra_pesquisa


class EntradasFrame(tk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.criar_componentes()
        self.carregar_dados()
