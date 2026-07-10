from database.database_service import DatabaseService


class FornecedorService:

    @staticmethod
    def listar_todos():

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            SELECT
                Id,
                Nome,
                Cnpj,
                Telefone,
                Contato,
                Email
            FROM Fornecedores
            WHERE Ativo = 1
            ORDER BY Nome
        """)

        dados = cursor.fetchall()

        conn.close()

        return dados

    @staticmethod
    def inserir(
        nome,
        cnpj,
        telefone,
        contato,
        email
    ):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO Fornecedores (
                Nome,
                Cnpj,
                Telefone,
                Contato,
                Email
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            nome,
            cnpj,
            telefone,
            contato,
            email
        ))

        conn.commit()
        conn.close()

    @staticmethod
    def excluir(id_registro):

        conn = DatabaseService.get_connection()

        cursor = conn.cursor()

        cursor.execute("""
            UPDATE Fornecedores
            SET Ativo = 0
            WHERE Id = ?
        """, (id_registro,))

        conn.commit()
        conn.close()

    @staticmethod
    def obter_por_id(id_registro):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Id,
                Nome,
                Cnpj,
                Telefone,
                Contato,
                Email
            FROM Fornecedores
            WHERE Id = ?
        """, (id_registro,))
    
        resultado = cursor.fetchone()
    
        conn.close()
    
        return resultado

    @staticmethod
    def atualizar(
        id_registro,
        nome,
        cnpj,
        telefone,
        contato,
        email
    ):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            UPDATE Fornecedores
            SET
                Nome = ?,
                Cnpj = ?,
                Telefone = ?,
                Contato = ?,
                Email = ?
            WHERE Id = ?
        """, (
            nome,
            cnpj,
            telefone,
            contato,
            email,
            id_registro
        ))
    
        conn.commit()
        conn.close()

    @staticmethod
    def pesquisar(texto):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT
                Id,
                Nome,
                Cnpj,
                Telefone,
                Contato,
                Email
            FROM Fornecedores
            WHERE
                UPPER(Nome) LIKE UPPER(?)
                OR UPPER(Cnpj) LIKE UPPER(?)
                OR UPPER(Contato) LIKE UPPER(?)
            ORDER BY Nome
        """, (
            f"%{texto}%",
            f"%{texto}%",
            f"%{texto}%"
        ))
    
        dados = cursor.fetchall()
    
        conn.close()
    
        return dados

    @staticmethod
    def obter_ou_criar(nome):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT Id
            FROM Fornecedores
            WHERE UPPER(Nome) = UPPER(?)
        """, (nome,))
    
        fornecedor = cursor.fetchone()
    
        if fornecedor:
    
            conn.close()
    
            return fornecedor[0]
    
        cursor.execute("""
            INSERT INTO Fornecedores (
                Nome
            )
            VALUES (?)
        """, (nome,))
    
        conn.commit()
    
        novo_id = cursor.lastrowid
    
        conn.close()
    
        return novo_id

    @staticmethod
    def pesquisar_nomes(texto):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT Nome
            FROM Fornecedores
            WHERE
                Ativo = 1
                AND UPPER(Nome) LIKE UPPER(?)
            ORDER BY Nome
        """, (f"{texto}%",))
    
        resultado = [
            linha[0]
            for linha in cursor.fetchall()
        ]
    
        conn.close()
    
        return resultado

    @staticmethod
    def pesquisar_nomes(texto):
    
        conn = DatabaseService.get_connection()
    
        cursor = conn.cursor()
    
        cursor.execute("""
            SELECT Nome
            FROM Fornecedores
            WHERE
                Ativo = 1
                AND UPPER(Nome) LIKE UPPER(?)
            ORDER BY Nome
        """, (f"{texto}%",))
    
        resultado = [
            linha[0]
            for linha in cursor.fetchall()
        ]
    
        conn.close()
    
        return resultado
