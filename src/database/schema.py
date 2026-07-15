SCHEMA_SQL = """
PRAGMA foreign_keys = ON;

-- =========================
-- USUÁRIOS
-- =========================

CREATE TABLE IF NOT EXISTS Usuarios (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Login TEXT NOT NULL UNIQUE,
    SenhaHash TEXT NOT NULL,
    Perfil TEXT NOT NULL,
    Ativo INTEGER NOT NULL DEFAULT 1,
    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- CONFIGURAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Configuracoes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NomeHospital TEXT,

    CaminhoBackup TEXT,

    UltimoBackup DATETIME,

    VersaoSistema TEXT
);

-- =========================
-- LICITAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Licitacoes (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroLicitacao TEXT NOT NULL,
    TipoLicitacao TEXT,

    Ata TEXT,

    Consignado INTEGER DEFAULT 0,
    Contrato TEXT,
    NumeroContrato TEXT,

    Processo TEXT,
    Vigencia TEXT,

    Fornecedor TEXT,
    Cnpj TEXT,

    CodConsig TEXT,
    CodItem TEXT NOT NULL,

    Sirep TEXT,

    NomeMaterial TEXT NOT NULL,

    QtdLicitada INTEGER NOT NULL,

    ValorUnd REAL NOT NULL,

    RP TEXT,
    SC TEXT,

    Especialidade TEXT,

    Ativo INTEGER DEFAULT 1,

    ValorTotalPregao REAL DEFAULT 0,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- TIPOS DE MOVIMENTAÇÃO
-- =========================

CREATE TABLE IF NOT EXISTS TiposMovimentacao (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    Nome TEXT NOT NULL UNIQUE
);

-- =========================
-- MOVIMENTAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Movimentacoes (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    DataMovimento DATETIME NOT NULL,

    NumeroLicitacao TEXT NOT NULL,

    CodItem TEXT NOT NULL,

    TipoMovimento TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    ValorUnitario REAL,

    DocumentoOrigem TEXT,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- NOTAS FISCAIS
-- =========================

CREATE TABLE IF NOT EXISTS NotasFiscais (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroNF TEXT NOT NULL,

    ChaveAcesso TEXT,

    DataNF DATETIME NOT NULL,

    Fornecedor TEXT NOT NULL,

    Cnpj TEXT,

    TipoNota TEXT NOT NULL,

    ValorTotal REAL,

    Status TEXT DEFAULT 'ABERTA',

    Observacao TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- ITENS DA NF
-- =========================

CREATE TABLE IF NOT EXISTS NotaItens (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NotaFiscalId INTEGER NOT NULL,

    CodItem TEXT NOT NULL,

    NomeItem TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    ValorUnitario REAL,

    ValorTotal REAL,

    FOREIGN KEY (NotaFiscalId)
    REFERENCES NotasFiscais(Id)
);

-- =========================
-- SOLICITAÇÕES
-- =========================

CREATE TABLE IF NOT EXISTS Solicitacoes (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroSolicitacao TEXT,

    DataSolicitacao DATETIME NOT NULL,

    Cirurgia TEXT,

    PacienteRegistro TEXT,

    Especialidade TEXT,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- ITENS SOLICITADOS
-- =========================

CREATE TABLE IF NOT EXISTS SolicitacaoItens (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    SolicitacaoId INTEGER NOT NULL,

    CodItem TEXT NOT NULL,

    NomeItem TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    Status TEXT NOT NULL CHECK (
        Status IN (
            'SOLICITADO',
            'RETIRADO',
            'UTILIZADO',
            'DEVOLVIDO',
            'EXTRAVIADO',
            'PAGO'
        )
    ),

    FOREIGN KEY (SolicitacaoId)
    REFERENCES Solicitacoes(Id)
);

-- =========================
-- AUDITORIA
-- =========================

CREATE TABLE IF NOT EXISTS Auditoria (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    Usuario TEXT NOT NULL,

    Acao TEXT NOT NULL,

    Tabela TEXT NOT NULL,

    RegistroId INTEGER,

    DataHora DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- FORNECEDORES
-- =========================

CREATE TABLE IF NOT EXISTS Fornecedores (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Cnpj TEXT,
    Telefone TEXT,
    Email TEXT,
    Contato TEXT,
    Ativo INTEGER DEFAULT 1,
    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- PACIENTES
-- =========================

CREATE TABLE IF NOT EXISTS Pacientes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Registro TEXT NOT NULL UNIQUE,
    Nome TEXT NOT NULL,
    DataNascimento TEXT,
    Ativo INTEGER DEFAULT 1,
    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- ENTRADAS
-- =========================

CREATE TABLE IF NOT EXISTS Entradas (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroNF TEXT,

    SerieNF TEXT,

    DataEmissao TEXT,

    DataEntrada TEXT NOT NULL,

    TipoEntrada TEXT NOT NULL,

    Fornecedor TEXT NOT NULL,

    CodItem TEXT NOT NULL,

    NomeMaterial TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    ValorTotalNF REAL,

    ValorUnitario REAL,

    Lote TEXT,

    SerieProduto TEXT,

    DataValidade TEXT,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- CONTROLES
-- =========================

CREATE TABLE IF NOT EXISTS EstoqueRastreado (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    LicitacaoItemId INTEGER,

    NumeroLicitacao TEXT NOT NULL,

    CodItem TEXT NOT NULL,

    NomeMaterial TEXT NOT NULL,

    Lote TEXT NOT NULL,

    CodigoUnico TEXT NOT NULL,

    CodigoBarras TEXT NOT NULL UNIQUE,

    Quantidade INTEGER NOT NULL DEFAULT 1,

    Status TEXT NOT NULL DEFAULT 'DISPONIVEL'
    CHECK (
        Status IN (
            'DISPONIVEL',
            'RETIRADO',
            'UTILIZADO',
            'DEVOLVIDO',
            'EXTRAVIADO',
            'PAGO'
        )
    ),

    PacienteId INTEGER,

    PacienteRegistro TEXT,

    PacienteNome TEXT,

    Sala TEXT,

    DataEntrada DATETIME DEFAULT CURRENT_TIMESTAMP,

    DataRetirada TEXT,

    DataUtilizacao TEXT,

    DataDevolucao TEXT,

    DataExtravio TEXT,

    DataPagamento TEXT,

    Observacao TEXT,

    FOREIGN KEY (LicitacaoItemId)
    REFERENCES Licitacoes(Id)

);

-- =========================
-- HISTÓRIOCO
-- =========================


CREATE TABLE IF NOT EXISTS HistoricoMovimentacao (

    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    EstoqueId INTEGER,

    NumeroLicitacao TEXT,

    CodItem TEXT,

    NomeMaterial TEXT,

    Lote TEXT,

    CodigoUnico TEXT,

    StatusAnterior TEXT,

    StatusNovo TEXT,

    PacienteNome TEXT,

    PacienteRegistro TEXT,

    Sala TEXT,

    Usuario TEXT,

    DataMovimento TEXT,

    Observacao TEXT

);
-- =========================
-- ÍNDICES
-- =========================

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_CODIGO
ON Licitacoes (CodItem);

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_FORNECEDOR
ON Licitacoes (Fornecedor);

CREATE INDEX IF NOT EXISTS IDX_LICITACOES_ATA
ON Licitacoes (Ata);

CREATE INDEX IF NOT EXISTS IDX_MOVIMENTACOES_ITEM
ON Movimentacoes (CodItem);

CREATE INDEX IF NOT EXISTS IDX_MOVIMENTACOES_LICITACAO
ON Movimentacoes (NumeroLicitacao);

CREATE INDEX IF NOT EXISTS IDX_FORNECEDORES_NOME
ON Fornecedores (Nome);

CREATE INDEX IF NOT EXISTS IDX_PACIENTES_REGISTRO
ON Pacientes (Registro);

CREATE INDEX IF NOT EXISTS IDX_PACIENTES_NOME
ON Pacientes (Nome);

CREATE INDEX IF NOT EXISTS IDX_ENTRADAS_CODIGO
ON Entradas (CodItem);

CREATE INDEX IF NOT EXISTS IDX_ENTRADAS_FORNECEDOR
ON Entradas (Fornecedor);

CREATE INDEX IF NOT EXISTS IDX_RASTREIO_CODIGO
ON EstoqueRastreado (CodigoBarras);

CREATE INDEX IF NOT EXISTS IDX_RASTREIO_LOTE
ON EstoqueRastreado (Lote);

CREATE INDEX IF NOT EXISTS IDX_RASTREIO_UNICO
ON EstoqueRastreado (CodigoUnico);

CREATE INDEX IF NOT EXISTS IDX_RASTREIO_STATUS
ON EstoqueRastreado (Status);

CREATE INDEX IF NOT EXISTS IDX_RASTREIO_PACIENTE
ON EstoqueRastreado (PacienteRegistro);
"""
