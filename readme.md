# 📊 Pipeline ETL de Indicadores Econômicos

## 📌 Descrição
Este projeto implementa um pipeline ETL completo para extração, transformação e carga de indicadores econômicos do Banco Central do Brasil.

Os dados são coletados via API pública, transformados com métricas analíticas e armazenados em banco PostgreSQL, com execução automatizada e incremental.

---

## 🚀 Tecnologias utilizadas

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- Schedule (automação)
- Logging

---

## ⚙️ Arquitetura do Projeto

1. **Extract**
   - Coleta dados da API do Banco Central
   - Indicadores: SELIC, IPCA, Dólar

2. **Transform**
   - Conversão de tipos
   - Ordenação temporal
   - Cálculo de métricas:
     - Variação percentual
     - Média móvel

3. **Load**
   - Armazenamento em PostgreSQL
   - Estratégia incremental (sem duplicação)

---

## 🔄 Automação

O pipeline é executado automaticamente utilizando scheduler em Python, permitindo atualização contínua dos dados.

---

## 📊 Dados processados

- Taxa SELIC
- Índice IPCA
- Cotação do Dólar

Fonte: API do Banco Central do Brasil

---

## 🔥 Diferenciais

- Pipeline ETL completo
- Integração com API real
- Persistência em banco relacional
- Carga incremental
- Logging estruturado
- Automação de execução

---

## ▶️ Como executar

```bash
pip install -r requirements.txt
python main.py