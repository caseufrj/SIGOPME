import tkinter as tk

from services.dashboard_service import DashboardService


class DashboardView(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Dashboard - SIGOPME")
        self.geometry("1200x700")

        self.criar_componentes()

    def criar_componentes(self):

        frame_cards = tk.Frame(self)
        frame_cards.pack(
            fill="x",
            padx=20,
            pady=20
        )

        self.lbl_atas = self.criar_card(
            frame_cards,
            "Atas Vigentes",
            DashboardService.total_atas_vigentes(),
            0
        )

        self.lbl_fornecedores = self.criar_card(
            frame_cards,
            "Fornecedores",
            DashboardService.total_fornecedores(),
            1
        )

        self.lbl_itens = self.criar_card(
            frame_cards,
            "Itens",
            DashboardService.total_itens(),
            2
        )

        self.lbl_consignacao = self.criar_card(
            frame_cards,
            "Em Consignação",
            DashboardService.total_em_consignacao(),
            3
        )

        self.lbl_pagamento = self.criar_card(
            frame_cards,
            "Em Pagamento",
            DashboardService.total_em_pagamento(),
            4
        )

        self.lbl_extraviado = self.criar_card(
            frame_cards,
            "Extraviados",
            DashboardService.total_extraviado(),
            5
        )

        self.lbl_financeiro = self.criar_card(
            frame_cards,
            "Saldo Financeiro",
            f"R$ {DashboardService.saldo_financeiro_total():,.2f}",
            6
        )

        frame_mov = tk.Frame(self)
        frame_mov.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        titulo = tk.Label(
            frame_mov,
            text="Últimas Movimentações",
            font=("Arial", 14, "bold")
        )

        titulo.pack(anchor="w")

        self.lista_movimentos = tk.Listbox(
            frame_mov,
            height=15
        )

        self.lista_movimentos.pack(
            fill="both",
            expand=True,
            pady=10
        )

        self.carregar_movimentacoes()

    def criar_card(
        self,
        parent,
        titulo,
        valor,
        coluna
    ):

        frame = tk.LabelFrame(
            parent,
            text=titulo,
            padx=20,
            pady=10
        )

        frame.grid(
            row=0,
            column=coluna,
            padx=5,
            pady=5
        )

        label = tk.Label(
            frame,
            text=str(valor),
            font=("Arial", 14, "bold")
        )

        label.pack()

        return label

    def carregar_movimentacoes(self):

        self.lista_movimentos.delete(
            0,
            tk.END
        )

        movimentacoes = (
            DashboardService
            .ultimas_movimentacoes()
        )

        for mov in movimentacoes:

            data = mov[0]
            item = mov[1]
            tipo = mov[2]
            quantidade = mov[3]
            usuario = mov[4]

            texto = (
                f"{data} | "
                f"{item} | "
                f"{tipo} | "
                f"Qtd: {quantidade} | "
                f"{usuario}"
            )

            self.lista_movimentos.insert(
                tk.END,
                texto
            )
``
