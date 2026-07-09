import tkinter as tk


def criar_barra_pesquisa(
    parent,
    callback=None
):

    frame = tk.Frame(parent)

    tk.Label(
        frame,
        text="Pesquisar:"
    ).pack(
        side="left",
        padx=(20, 5)
    )

    txt_pesquisa = tk.Entry(
        frame,
        width=40
    )

    txt_pesquisa.pack(
        side="left"
    )

    if callback:

        txt_pesquisa.bind(
            "<KeyRelease>",
            callback
        )

    return frame, txt_pesquisa
