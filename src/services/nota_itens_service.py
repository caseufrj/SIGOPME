from database.database_service import DatabaseService


class NotaItensService:

    @staticmethod
    def inserir(
        entrada_id,
        cod_item,
        nome_item,
        lote,
        serie_produto,
        data_validade,
        quantidade,
        valor_unitario,
        valor_total
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO NotaItens (

                EntradaId,
                CodItem,
                NomeItem,
                Lote,
                SerieProduto,
                DataValidade,
                Quantidade,
                ValorUnitario,
                ValorTotal
            
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
        
            (
                entrada_id,    
                cod_item,
                nome_item,
                lote,
                serie_produto,
                data_validade,
                quantidade,
                valor_unitario,
                valor_total
            
        ))
    
        conn.commit()

        conn.close()
