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

        self.lbl_resultado = tk.Label(
            self,
            text="Nenhum item localizado.",
            justify="left"
        )

        self.lbl_resultado.pack(
            anchor="w",
            padx=10,
            pady=20
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

            self.lbl_resultado.config(
                text="Item não encontrado."
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
            *
        ) = resultado

        self.lbl_resultado.config(
            text=
            f"Licitação: {numero_licitacao}\n"
            f"Código: {cod_item}\n"
            f"Material: {nome_material}\n"
            f"Lote: {lote}\n"
            f"Código Único: {codigo_unico}\n"
            f"Status: {status}\n"
            f"Paciente: {paciente_nome or '-'}\n"
            f"Registro: {paciente_registro or '-'}\n"
            f"Sala: {sala or '-'}"
        )
