import tkinter as tk


def aplicar_mascara_data(entry):

    from datetime import datetime
    import tkinter as tk
    
    
    import tkinter as tk
from datetime import datetime
from tkinter import messagebox


def aplicar_mascara_data(entry):

    def ao_entrar(event):

        if not entry.get():

            entry.insert(
                0,
                "__/__/____"
            )

            entry.icursor(0)

    def ao_digitar(event):

        numeros = "".join(
            c
            for c in entry.get()
            if c.isdigit()
        )[:8]

        texto = "__/__/____"

        lista = list(texto)

        posicoes = [
            0, 1,
            3, 4,
            6, 7, 8, 9
        ]

        for i, numero in enumerate(numeros):

            if i < len(posicoes):

                lista[
                    posicoes[i]
                ] = numero

        texto = "".join(lista)

        entry.delete(
            0,
            tk.END
        )

        entry.insert(
            0,
            texto
        )

        if len(numeros) < 8:

            entry.icursor(
                posicoes[len(numeros)]
            )

    def validar(event):

        valor = entry.get()

        if valor == "__/__/____":

            entry.delete(
                0,
                tk.END
            )

            return

        if "_" in valor:

            messagebox.showwarning(
                "SIGOPME",
                "Data incompleta."
            )

            entry.focus_set()

            return

        try:

            datetime.strptime(
                valor,
                "%d/%m/%Y"
            )

        except ValueError:

            messagebox.showwarning(
                "SIGOPME",
                "Data inválida."
            )

            entry.focus_set()

    entry.bind(
        "<FocusIn>",
        ao_entrar
    )

    entry.bind(
        "<KeyRelease>",
        ao_digitar
    )

    entry.bind(
        "<FocusOut>",
        validar
    )


def aplicar_mascara_moeda(entry):

    def ao_entrar(event):

        if not entry.get():

            entry.insert(
                0,
                "R$ 0,00"
            )

    def ao_digitar(event):

        valor = "".join(
            c
            for c in entry.get()
            if c.isdigit()
        )

        if not valor:

            valor = "0"

        numero = int(valor)

        numero /= 100

        texto = (
            f"R$ {numero:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        entry.delete(
            0,
            tk.END
        )

        entry.insert(
            0,
            texto
        )

        entry.icursor(
            tk.END
        )

    entry.bind(
        "<FocusIn>",
        ao_entrar
    )

    entry.bind(
        "<KeyRelease>",
        ao_digitar
    )
