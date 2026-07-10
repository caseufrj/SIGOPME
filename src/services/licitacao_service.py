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
                NumeroLicitacao,
                Ata,
                Fornecedor,
                TipoLicitacao,
                CodItem,
                NomeMaterial,
                QtdLicitada,
                ValorUnd,
    
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
                CodItem,
                NomeMaterial,
                QtdLicitada,
                ValorUnd
            FROM Licitacoes
            WHERE Id = ?
        """, (id_registro,))
    
        resultado = cursor.fetchone()
    
        conn.close()
    
        return resultado

    @staticmethod
    def atualizar(
        id_registro,
        licitacao,
        ata,
        fornecedor,
        tipo_licitacao,
        codigo_item,
        nome_material,
        quantidade,
        valor
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
                CodItem = ?,
                NomeMaterial = ?,
                QtdLicitada = ?,
                ValorUnd = ?
            WHERE Id = ?
        """, (
            licitacao,
            ata,
            fornecedor,
            tipo_licitacao,
            codigo_item,
            nome_material,
            quantidade,
            valor,
            id_registro
        ))
    
        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id_registro):
    
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
    def inserir(
        licitacao,
        ata,
        fornecedor,
        tipo_licitacao,
        codigo_item,
        nome_material,
        quantidade,
        valor
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
                CodItem,
                NomeMaterial,
                QtdLicitada,
                ValorUnd
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            licitacao,
            ata,
            fornecedor,
            tipo_licitacao,
            codigo_item,
            nome_material,
            quantidade,
            valor
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
 
