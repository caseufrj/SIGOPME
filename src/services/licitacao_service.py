from database.database_service import DatabaseService
from services.fornecedor_service import FornecedorService

class LicitacaoService:

    @staticmethod
    def listar_todos():
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Id,
                Licitacao,
                Ata,
                Fornecedor,
                Tipo,
                consignado,
    
                QtdLicitada AS SaldoPedido,
    
                (QtdLicitada * ValorUnd) AS SaldoFinanceiro,
    
                0 AS Consignacao,
                0 AS Retirado,
                0 AS Utilizado,
                0 AS EmPagamento,
                0 AS Pago
    
            FROM Licitacoes
            WHERE Ativo = 1
            ORDER BY NumeroLicitacao
        """)
    
        resultado = cursor.fetchall()
    
        conn.close()
    
        return resultado

    @staticmethod
    def buscar_por_codigo(codigo):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE CodItem LIKE ?
        """, (f"%{codigo}%",))

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def buscar_por_fornecedor(fornecedor):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE Fornecedor LIKE ?
        """, (f"%{fornecedor}%",))

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def buscar_por_ata(ata):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE Ata LIKE ?
        """, (f"%{ata}%",))

        resultado = cursor.fetchall()

        conn.close()

        return resultado

    @staticmethod
    def pesquisar(texto):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Fornecedor,
                Ata,
                QtdLicitada
            FROM Licitacoes
            WHERE
                UPPER(CodItem) LIKE UPPER(?)
                OR UPPER(NomeMaterial) LIKE UPPER(?)
                OR UPPER(Fornecedor) LIKE UPPER(?)
                OR UPPER(Ata) LIKE UPPER(?)
            ORDER BY NomeMaterial
        """, (
            f"%{texto}%",
            f"%{texto}%",
            f"%{texto}%",
            f"%{texto}%"
        ))
    
        resultado = cursor.fetchall()
    
        conn.close()
    
        return resultado

    
    @staticmethod
    def obter_por_id(id_registro):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Id,
                NumeroLicitacao,
                Ata,
                Fornecedor,
                TipoLicitacao,
                Consignado,
                ValorTotalPregao
            FROM Licitacoes
            WHERE Id = ?
        """, (id_registro,))
    
        resultado = cursor.fetchone()
    
        conn.close()
    
        return resultado

    @staticmethod
    def atualizar_licitacao(
        id_registro,
        licitacao,
        ata,
        fornecedor,
        tipo,
        consignado,
        valor_total
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Licitacoes
            SET
                NumeroLicitacao = ?,
                Ata = ?,
                Fornecedor = ?,
                TipoLicitacao = ?,
                Consignado = ?,
                ValorTotalPregao = ?
            WHERE Id = ?
        """, (
            licitacao,
            ata,
            fornecedor,
            tipo,
            consignado,
            valor_total,
            id_registro
        ))
    
        conn.commit()
        conn.close()

    @staticmethod
    def excluir_licitacao(id_registro):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Licitacoes
            SET Ativo = 0
            WHERE Id = ?
        """, (id_registro,))
    
        conn.commit()
        conn.close()

    @staticmethod
    def inserir_licitacao(
        licitacao,
        ata,
        fornecedor,
        tipo_licitacao,
        consignado,
        valor_total
    ):
    
        FornecedorService.obter_ou_criar(
            fornecedor
        )
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            INSERT INTO Licitacoes (
                NumeroLicitacao,
                Ata,
                Fornecedor,
                TipoLicitacao,
                Consignado,
                ValorTotalPregao,
                CodItem,
                NomeMaterial,
                QtdLicitada,
                ValorUnd
            )
            VALUES (?, ?, ?, ?, ?, ?, '', '', 0, 0)
        """, (
            licitacao,
            ata,
            fornecedor,
            tipo_licitacao,
            consignado,
            valor_total
        ))
    
        conn.commit()
    
        conn.close()

    @staticmethod
    def obter_por_codigo(codigo):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Fornecedor,
                NomeMaterial,
                ValorUnd
            FROM Licitacoes
            WHERE CodItem = ?
            LIMIT 1
        """, (codigo,))
    
        resultado = cursor.fetchone()
    
        conn.close()
    
        return resultado

    @staticmethod
    def listar_resumo_licitacoes():
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                MIN(Id) AS Id,
    
                NumeroLicitacao,
    
                MAX(Ata) AS Ata,
    
                MAX(Fornecedor) AS Fornecedor,
    
                MAX(TipoLicitacao) AS TipoLicitacao,
    
                MAX(Consignado) AS Consignado,
    
                MAX(ValorTotalPregao) AS ValorTotal
    
            FROM Licitacoes
    
            WHERE Ativo = 1
    
            GROUP BY NumeroLicitacao
    
            ORDER BY NumeroLicitacao
        """)
    
        resultado = cursor.fetchall()
    
        conn.close()
    
        return resultado

    @staticmethod
    def listar_itens_licitacao(numero_licitacao):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT

                Id,
            
                CodItem,
            
                NomeMaterial,
            
                QtdLicitada,
            
                ValorUnd,
            
                QtdLicitada AS SaldoPedido,
            
                QtdLicitada AS SaldoFinanceiro,
            
                0 AS Consignacao,
            
                0 AS Retirado,
            
                0 AS Utilizado,
            
                0 AS EmPagamento,
            
                0 AS Pago
    
            FROM Licitacoes
    
            WHERE
                NumeroLicitacao = ?
                AND Ativo = 1
                AND CodItem <> ''
    
            ORDER BY CodItem
        """, (numero_licitacao,))
    
        resultado = cursor.fetchall()
    
        conn.close()
    
        return resultado

    @staticmethod
    def excluir_licitacao(numero_licitacao):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Licitacoes
            SET Ativo = 0
            WHERE NumeroLicitacao = ?
        """, (
            numero_licitacao,
        ))
    
        conn.commit()
    
        conn.close()

    @staticmethod
    def inserir_item(
        numero_licitacao,
        codigo_item,
        nome_material,
        qtd_licitada,
        valor_unitario
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Ata,
                Fornecedor,
                TipoLicitacao,
                Consignado,
                ValorTotalPregao
            FROM Licitacoes
            WHERE NumeroLicitacao = ?
            LIMIT 1
        """, (numero_licitacao,))
    
        dados = cursor.fetchone()
    
        ata, fornecedor, tipo, consignado, valor_total = dados
    
        cursor.execute("""
            INSERT INTO Licitacoes (
    
                NumeroLicitacao,
                Ata,
                Fornecedor,
                TipoLicitacao,
                Consignado,
                ValorTotalPregao,
    
                CodItem,
                NomeMaterial,
                QtdLicitada,
                ValorUnd,
    
                Ativo
    
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            numero_licitacao,
            ata,
            fornecedor,
            tipo,
            consignado,
            valor_total,
    
            codigo_item,
            nome_material,
            qtd_licitada,
            valor_unitario
        ))
    
        conn.commit()
    
        conn.close()

    @staticmethod
    def obter_item(id_item):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                Id,
                CodItem,
                NomeMaterial,
                QtdLicitada,
                ValorUnd
    
            FROM Licitacoes
    
            WHERE Id = ?
        """, (id_item,))
    
        resultado = cursor.fetchone()
    
        conn.close()
    
        return resultado

    @staticmethod
    def atualizar_item(
        id_item,
        codigo_item,
        nome_material,
        qtd_licitada,
        valor_unitario
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Licitacoes
            SET
    
                CodItem = ?,
                NomeMaterial = ?,
                QtdLicitada = ?,
                ValorUnd = ?
    
            WHERE Id = ?
        """, (
            codigo_item,
            nome_material,
            qtd_licitada,
            valor_unitario,
            id_item
        ))
    
        conn.commit()
    
        conn.close()

    @staticmethod
    def excluir_item(id_item):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Licitacoes
            SET Ativo = 0
            WHERE Id = ?
        """, (id_item,))
    
        conn.commit()
    
        conn.close()

    @staticmethod
    def listar_licitacoes_fornecedor(
        fornecedor
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT DISTINCT
                NumeroLicitacao
            FROM Licitacoes
            WHERE
                Fornecedor = ?
                AND Ativo = 1
            ORDER BY NumeroLicitacao
        """, (fornecedor,))
    
        resultado = cursor.fetchall()
    
        conn.close()
    
        return resultado

    @staticmethod
    def listar_itens_entrada(
        numero_licitacao
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Id,
                CodItem,
                NomeMaterial,
                ValorUnd
            FROM Licitacoes
            WHERE
                NumeroLicitacao = ?
                AND Ativo = 1
                AND CodItem <> ''
            ORDER BY NomeMaterial
        """, (numero_licitacao,))
    
        resultado = cursor.fetchall()
    
        conn.close()
    
        return resultado

   
