import tkinter as tk


def aplicar_mascara_data(entry):

    def ao_digitar(event):

        valor = "".join(
            filter(str.isdigit, entry.get())
        )

        valor = valor[:8]

        texto = ""

        if len(valor) >= 1:
            texto += valor[:2]

        if len(valor) >= 3:
            texto = valor[:2] + "/" + valor[2:4]

        if len(valor) >= 5:
            texto = (
                valor[:2]
                + "/"
                + valor[2:4]
                + "/"
                + valor[4:8]
            )

        entry.delete(0, tk.END)
        entry.insert(0, texto)

    entry.bind(
        "<KeyRelease>",
        ao_digitar
    )


def aplicar_mascara_moeda(entry):

    def ao_digitar(event):

        valor = "".join(
            filter(str.isdigit, entry.get())
        )

        if not valor:
            valor = "0"

        numero = int(valor) / 100

        texto = (
            f"{numero:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        entry.delete(0, tk.END)
        entry.insert(0, texto)

    entry.bind(
        "<KeyRelease>",
        ao_digitar
    )
