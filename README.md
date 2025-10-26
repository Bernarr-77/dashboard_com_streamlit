# 🍞 Dashboard de Análise de Vendas - Padaria do Seu Zé

## 🎯 Visão Geral

Este projeto consiste em um dashboard de análise de vendas construído em Python, utilizando o framework **Streamlit** para criação da interface web interativa. O foco é transformar dados brutos de transações em *insights* de negócio, permitindo a visualização clara de métricas-chave de desempenho (KPIs) e a filtragem dinâmica da base de dados.

## ⚙️ Funcionalidades e Recursos

O dashboard está estruturado para oferecer uma análise completa do desempenho da padaria:

### 1. Filtros Dinâmicos (Sidebar)
* **Filtro de Período:** Seleção da data inicial e final das vendas.
* **Filtros Categoria/Pagamento:** Seleção múltipla por Categoria de Produto e Forma de Pagamento.

### 2. Indicadores-Chave de Desempenho (KPIs)
Os principais indicadores são apresentados em tempo real, com formatação correta para o padrão brasileiro (separador de milhar e centavos):
* **Total de Vendas (R$):** Faturamento total do período.
* **Valor Médio de Compra (Ticket Médio):** Valor médio por transação.
* **Total de Produtos Vendidos:** Quantidade total de itens.
* **Produto Mais Vendido:** Identifica o item de maior volume de vendas.

### 3. Visualizações Profissionais (Altair)
Os gráficos são construídos com a biblioteca Altair, oferecendo interatividade (`.interactive()`) e tooltips (detalhes ao passar o mouse):
* **Gráfico de Barras:** Total vendido por Categoria de Produto.
* **Gráfico de Linha:** Evolução diária de vendas (faturamento ao longo do tempo).
* **Gráfico de Arco (Pizza):** Distribuição das vendas por Forma de Pagamento.

### 4. Tabela de Dados e Exportação
* Exibição da tabela de dados (`df_filtrado`) com os filtros aplicados.
* Botão de **Download** para exportar os dados exatamente como foram filtrados para um arquivo CSV.

## 🚀 Como Rodar o Projeto Localmente

### Pré-requisitos
Certifique-se de ter o Python instalado (versão 3.8+).

### 1. Instalação das Dependências

Instale as bibliotecas necessárias usando o `pip`:

```bash
pip install streamlit pandas altair
