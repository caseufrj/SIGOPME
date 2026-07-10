import tkinter as tk


def aplicar_mascara_data(entry):

    from datetime import datetime
    import tkinter as tk
    
    
    def aplicar_mascara_data(entry):
    
        def ao_digitar(event):
    
            valor = "".join(
                filter(str.isdigit, entry.get())
            )
    
            valor = valor[:8]
    
            if len(valor) <= 2:
                texto = valor
    
            elif len(valor) <= 4:
                texto = (
                    valor[:2]
                    + "/"
                    + valor[2:]
                )
    
            else:
                texto = (
                    valor[:2]
                    + "/"
                    + valor[2:4]
                    + "/"
                    + valor[4:]
                )
    
            entry.delete(0, tk.END)
            entry.insert(0, texto)
    
        def validar(event):
    
            valor = entry.get().strip()
    
            if not valor:
                return
    
            try:
    
                datetime.strptime(
                    valor,
                    "%d/%m/%Y"
                )
    
            except ValueError:
    
                entry.delete(
                    0,
                    tk.END
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
