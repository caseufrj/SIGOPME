from database.database_service import DatabaseService


class NotaItensService:

    @staticmethod
    def inserir(
        nota_fiscal_id,
        cod_item,
        nome_item,
        quantidade,
        valor_unitario,
        valor_total
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO NotaItens (

                NotaFiscalId,
                CodItem,
                NomeItem,
                Quantidade,
                ValorUnitario,
                ValorTotal

            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (

            nota_fiscal_id,
            cod_item,
            nome_item,
            quantidade,
            valor_unitario,
            valor_total

        ))

        conn.commit()

        conn.close()
