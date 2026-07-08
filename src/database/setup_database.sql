PRAGMA foreign_keys = ON;

-- ==========================================
-- SIGOPME
-- INSTALAÇÃO INICIAL DO BANCO
-- ==========================================

-- 1. CRIAÇÃO DAS TABELAS
.read create_database.sql

-- 2. CRIAÇÃO DAS VIEWS
.read views.sql

-- 3. DADOS INICIAIS
.read seed_data.sql
