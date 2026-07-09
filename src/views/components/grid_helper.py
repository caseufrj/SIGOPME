import tkinter as tk
from tkinter import ttk


def criar_treeview(parent, colunas):

    frame = tk.Frame(parent)

    scroll_y = ttk.Scrollbar(
        frame,
        orient="vertical"
    )

    scroll_x = ttk.Scrollbar(
        frame,
        orient="horizontal"
    )

    tree = ttk.Treeview(
        frame,
        columns=colunas,
        show="headings",
        yscrollcommand=scroll_y.set,
        xscrollcommand=scroll_x.set
    )

    scroll_y.config(
        command=tree.yview
    )

    scroll_x.config(
        command=tree.xview
    )

    scroll_y.pack(
        side="right",
        fill="y"
    )

    scroll_x.pack(
        side="bottom",
        fill="x"
    )

    tree.pack(
        side="left",
        fill="both",
        expand=True
    )

    return frame, tree
