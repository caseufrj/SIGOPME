from database.database_service import DatabaseService


class MovimentacaoService:

    @staticmethod
    def registrar_movimentacao(
        numero_licitacao,
        cod_item,
        tipo_movimento,
        quantidade,
        usuario,
        observacao=None,
        documento_origem=None
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Movimentacoes (
                DataMovimento,
                NumeroLicitacao,
                CodItem,
                TipoMovimento,
                Quantidade,
                DocumentoOrigem,
                Observacao,
                Usuario
            )
            VALUES (
                datetime('now'),
                ?, ?, ?, ?, ?, ?, ?
            )
            """,
            (
                numero_licitacao,
                cod_item,
                tipo_movimento,
                quantidade,
                documento_origem,
                observacao,
                usuario
            )
        )

        conn.commit()
        conn.close()
