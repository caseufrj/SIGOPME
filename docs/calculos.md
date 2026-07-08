# SIGOPME - Cálculos

Todos os saldos do sistema serão calculados a partir das movimentações.

Nenhum saldo será armazenado diretamente no banco.

---

# Saldo Pedido

Fórmula:

Qtd Licitada
- Entrada Consignação
- Entrada Venda

Exemplo:

Qtd Licitada = 100

Entrada Consignação = 20

Entrada Venda = 10

Saldo Pedido = 70

---

# Em Consignação

Fórmula:

Entrada Consignação
- Utilizado
- Devolvido
- Extraviado

Exemplo:

Entrada Consignação = 20

Utilizado = 5

Devolvido = 3

Extraviado = 2

Em Consignação = 10

---

# Retirado

Fórmula:

Soma de todas as movimentações RETIRADO

---

# Utilizado

Fórmula:

Soma de todas as movimentações UTILIZADO

---

# Devolvido

Fórmula:

Soma de todas as movimentações DEVOLVIDO

---

# Extraviado

Fórmula:

Soma de todas as movimentações EXTRAVIADO

---

# Pago

Fórmula:

Soma de todas as movimentações PAGO

---

# Em Pagamento

Fórmula:

Utilizado
- Pago

Exemplo:

Utilizado = 12

Pago = 8

Em Pagamento = 4

---

# Saldo Financeiro

Fórmula:

(Qtd Licitada × Valor Unitário)
-
(Pago × Valor Unitário)
-
(Extraviado × Valor Unitário)

Exemplo:

Qtd Licitada = 100

Valor Unitário = 50

Pago = 20

Extraviado = 2

Saldo Financeiro =

5000
-
1000
-
100

= 3900
