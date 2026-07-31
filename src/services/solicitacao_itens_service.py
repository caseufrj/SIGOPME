from database.database_service import DatabaseService


class SolicitacaoItensService:

    @staticmethod
    def inserir(
        solicitacao_id,
        cod_item,
        nome_item,
        lote,
        quantidade
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO SolicitacaoItens (
        
                SolicitacaoId,
                CodItem,
                NomeItem,
                Lote,
                Quantidade,
                QuantidadeAtendida,
                Status
        
            )
            VALUES (
        
                ?, ?, ?, ?, ?, 0,
                'SOLICITADO'
        
            )
        """, (
        
            solicitacao_id,
            cod_item,
            nome_item,
            lote,
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
                Lote,
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

    @staticmethod
    def obter_por_protocolo(
        solicitacao_id
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                Id,
                Status
    
            FROM SolicitacaoItens
    
            WHERE SolicitacaoId = ?
    
            LIMIT 1
        """, (solicitacao_id,))

            
        dados = cursor.fetchone()

        print("SolicitacaoItens =", dados)
    
        conn.close()
    
        return dados
