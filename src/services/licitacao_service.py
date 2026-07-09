from database.database_service import DatabaseService


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
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            INSERT INTO Licitacoes (
                NumeroLicitacao,
                Ata,
                CodItem,
                NomeMaterial,
                Fornecedor,
                QtdLicitada,
                ValorUnd
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            numero_licitacao,
            ata,
            codigo,
            descricao,
            fornecedor,
            quantidade,
            valor
        ))
    
        conn.commit()
        conn.close()

    @staticmethod
    def listar_todos():
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Id,
                NumeroLicitacao,
                Ata,
                CodItem,
                NomeMaterial,
                Fornecedor,
                QtdLicitada,
                ValorUnd
            FROM Licitacoes
            WHERE Ativo = 1
            ORDER BY NomeMaterial
        """)
    
        dados = cursor.fetchall()
    
        conn.close()
    
        return dados
