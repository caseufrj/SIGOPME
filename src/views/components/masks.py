import tkinter as tk
from datetime import datetime
from tkinter import messagebox


def aplicar_mascara_data(entry):

    def ao_digitar(event):

        texto = (
            entry.get()
            .replace("/", "")
        )

        if not texto:
            return

        texto = "".join(
            c for c in texto
            if c.isdigit()
        )[:8]

        resultado = ""

        if len(texto) >= 1:
            resultado = texto[:2]

        if len(texto) > 2:
            resultado += "/" + texto[2:4]

        if len(texto) > 4:
            resultado += "/" + texto[4:8]

        cursor = entry.index(tk.INSERT)

        entry.delete(
            0,
            tk.END
        )

        entry.insert(
            0,
            resultado
        )

        try:
            entry.icursor(cursor)
        except:
            pass

    def validar(event):

        valor = entry.get().strip()
    
        if not valor:
            return
    
        # 2807 -> 28/07/2026
        if valor.isdigit() and len(valor) == 4:
    
            valor = (
                f"{valor[:2]}/"
                f"{valor[2:]}/"
                f"{datetime.now().year}"
            )
    
            entry.delete(0, tk.END)
    
            entry.insert(0, valor)
    
        # 28/07 -> 28/07/2026
        elif len(valor) == 5:
    
            valor = (
                f"{valor}/"
                f"{datetime.now().year}"
            )
    
            entry.delete(0, tk.END)
    
            entry.insert(0, valor)
    
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
