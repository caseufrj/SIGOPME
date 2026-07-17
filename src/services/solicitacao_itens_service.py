from database.database_service import DatabaseService


class SolicitacaoItensService:

    @staticmethod
    def inserir(
        solicitacao_id,
        cod_item,
        nome_item,
        quantidade
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO SolicitacaoItens (

                SolicitacaoId,
                CodItem,
                NomeItem,
                Quantidade,
                QuantidadeAtendida,
                Status

            )
            VALUES (

                ?, ?, ?, ?, 0,
                'SOLICITADO'

            )
        """, (

            solicitacao_id,
            cod_item,
            nome_item,
            quantidade

        ))

        conn.commit()

        conn.close()


    @staticmethod
    def listar_por_solicitacao(
        solicitacao_id
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT

                Id,
                CodItem,
                NomeItem,
                Quantidade,
                QuantidadeAtendida,
                Status

            FROM SolicitacaoItens

            WHERE SolicitacaoId = ?

            ORDER BY NomeItem
        """, (solicitacao_id,))

        dados = cursor.fetchall()

        conn.close()

        return dados


    @staticmethod
    def excluir_por_solicitacao(
        solicitacao_id
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            DELETE
            FROM SolicitacaoItens
            WHERE SolicitacaoId = ?
        """, (solicitacao_id,))

        conn.commit()

        conn.close()


    @staticmethod
    def atualizar_status(
        item_id,
        status
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE SolicitacaoItens
            SET Status = ?
            WHERE Id = ?
        """, (
            status,
            item_id
        ))

        conn.commit()

        conn.close()


    @staticmethod
    def atualizar_quantidade_atendida(
        item_id,
        quantidade
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE SolicitacaoItens
            SET QuantidadeAtendida = ?
            WHERE Id = ?
        """, (
            quantidade,
            item_id
        ))

        conn.commit()

        conn.close()
