from database.database_service import DatabaseService
from services.fornecedor_service import FornecedorService


class EntradaService:
    @staticmethod
    def listar_todos():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                NumeroLicitacao,
                NumeroNF,
                SerieNF,
                DataEmissao,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                ValorTotalNF
            FROM Entradas
            ORDER BY DataEntrada DESC
        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    @staticmethod
    def inserir(
        numero_nf,
        serie_nf,
        data_emissao,
        data_entrada,
        tipo_entrada,
        fornecedor,
        valor_nf,
        observacao,
        numero_licitacao
    ):
    
        FornecedorService.obter_ou_criar(
            fornecedor
        )
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            INSERT INTO Entradas (
        
                NumeroLicitacao,
                NumeroNF,
                SerieNF,
                DataEmissao,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                ValorTotalNF,
                Observacao
        
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
        
            numero_licitacao,
            numero_nf,
            serie_nf,
            data_emissao,
            data_entrada,
            tipo_entrada,
            fornecedor,
            valor_nf,
            observacao
        
        ))
        nota_id = cursor.lastrowid

        conn.commit()
        
        conn.close()
        
        return nota_id

    @staticmethod
    def obter_por_id(id_registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                NumeroLicitacao,
                NumeroNF,
                SerieNF,
                DataEmissao,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                ValorTotalNF,
                Observacao
            FROM Entradas
            WHERE Id = ?
        """, (id_registro,))

        resultado = cursor.fetchone()

        conn.close()

        return resultado

    @staticmethod
    def atualizar(
        id_entrada,
        numero_licitacao,
        numero_nf,
        serie_nf,
        data_emissao,
        data_entrada,
        tipo_entrada,
        fornecedor,
        valor_total_nf,
        observacao
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Entradas
            SET
    
                NumeroLicitacao = ?,
                NumeroNF = ?,
                SerieNF = ?,
                DataEmissao = ?,
                DataEntrada = ?,
                TipoEntrada = ?,
                Fornecedor = ?,
                ValorTotalNF = ?,
                Observacao = ?
    
            WHERE Id = ?
        """, (
    
            numero_licitacao,
            numero_nf,
            serie_nf,
            data_emissao,
            data_entrada,
            tipo_entrada,
            fornecedor,
            valor_total_nf,
            observacao,
            id_entrada
    
        ))
    
        conn.commit()
    
        conn.close()

    @staticmethod
    def excluir(id_registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM Entradas
            WHERE Id = ?
        """, (id_registro,))

        conn.commit()

        conn.close()

    @staticmethod
    def listar_itens_nf(numero_nf):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                CodItem,
                NomeMaterial,
                Lote,
                CodigoUnico,
                DataValidade,
                Quantidade,
                Status
            FROM EstoqueRastreado
    
            WHERE NumeroNF = ?
    
            ORDER BY NomeMaterial
    
        """, (numero_nf,))
    
        dados = cursor.fetchall()
    
        conn.close()
    
        return dados

    @staticmethod
    def obter_por_id(id_entrada):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                Id,
                NumeroLicitacao,
                NumeroNF,
                SerieNF,
                DataEmissao,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                ValorTotalNF,
                Observacao
    
            FROM Entradas
    
            WHERE Id = ?
        """, (id_entrada,))
    
        dados = cursor.fetchone()
    
        conn.close()
    
        return dados

    @staticmethod
    def listar_por_entrada(entrada_id):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
    
                CodItem,
                NomeItem,
                Lote,
                SerieProduto,
                DataValidade,
                Quantidade,
                ValorUnitario,
                ValorTotal
    
            FROM NotaItens
    
            WHERE EntradaId = ?
    
            ORDER BY NomeItem
        """, (entrada_id,))
    
        dados = cursor.fetchall()
    
        conn.close()
    
        return dados
