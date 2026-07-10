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
                NumeroNF,
                SerieNF,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                CodItem,
                NomeMaterial,
                Quantidade
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
        codigo_item,
        nome_material,
        quantidade,
        observacao
    ):
        FornecedorService.obter_ou_criar(
            fornecedor
        )
        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Entradas (
                NumeroNF,
                SerieNF,
                DataEmissao,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                CodItem,
                NomeMaterial,
                Quantidade,
                Observacao
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            numero_nf,
            serie_nf,
            data_emissao,
            data_entrada,
            tipo_entrada,
            fornecedor,
            codigo_item,
            nome_material,
            quantidade,
            observacao
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def obter_por_id(id_registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                NumeroNF,
                SerieNF,
                DataEmissao,
                DataEntrada,
                TipoEntrada,
                Fornecedor,
                CodItem,
                NomeMaterial,
                Quantidade,
                Observacao
            FROM Entradas
            WHERE Id = ?
        """, (id_registro,))

        resultado = cursor.fetchone()

        conn.close()

        return resultado

    @staticmethod
    def atualizar(
        id_registro,
        numero_nf,
        serie_nf,
        data_emissao,
        data_entrada,
        tipo_entrada,
        fornecedor,
        codigo_item,
        nome_material,
        quantidade,
        observacao
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Entradas
            SET
                NumeroNF = ?,
                SerieNF = ?,
                DataEmissao = ?,
                DataEntrada = ?,
                TipoEntrada = ?,
                Fornecedor = ?,
                CodItem = ?,
                NomeMaterial = ?,
                Quantidade = ?,
                Observacao = ?
            WHERE Id = ?
        """, (
            numero_nf,
            serie_nf,
            data_emissao,
            data_entrada,
            tipo_entrada,
            fornecedor,
            codigo_item,
            nome_material,
            quantidade,
            observacao,
            id_registro
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
