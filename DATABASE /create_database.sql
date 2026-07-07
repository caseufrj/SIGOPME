CREATE TABLE Licitacoes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroLicitacao TEXT NOT NULL,
    TipoLicitacao TEXT,

    Ata TEXT,

    Consignado TEXT,
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

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Movimentacoes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    DataMovimento DATETIME NOT NULL,

    NumeroLicitacao TEXT NOT NULL,

    CodItem TEXT NOT NULL,

    TipoMovimento TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE NotasFiscais (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroNF TEXT NOT NULL,

    DataNF DATETIME NOT NULL,

    Fornecedor TEXT NOT NULL,

    Cnpj TEXT,

    TipoNota TEXT NOT NULL,

    ValorTotal REAL,

    Observacao TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE NotaItens (
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

CREATE TABLE Solicitacoes (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    NumeroSolicitacao TEXT,

    DataSolicitacao DATETIME NOT NULL,

    Especialidade TEXT,

    Observacao TEXT,

    Usuario TEXT,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE SolicitacaoItens (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    SolicitacaoId INTEGER NOT NULL,

    CodItem TEXT NOT NULL,

    NomeItem TEXT NOT NULL,

    Quantidade INTEGER NOT NULL,

    Status TEXT NOT NULL,

    FOREIGN KEY (SolicitacaoId)
        REFERENCES Solicitacoes(Id)
);

CREATE TABLE Usuarios (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,

    Nome TEXT NOT NULL,

    Login TEXT NOT NULL UNIQUE,

    SenhaHash TEXT NOT NULL,

    Perfil TEXT NOT NULL,

    Ativo INTEGER NOT NULL DEFAULT 1,

    DataCriacao DATETIME DEFAULT CURRENT_TIMESTAMP
);
