import streamlit as st
import pandas as pd
import altair as alt


@st.cache_data
def carregar_dados():
    df = pd.read_csv("vendas_padaria.csv")
    df['Data'] = pd.to_datetime(df["Data"])
    df['total_vendas'] = df['Quantidade'] * df['Preço_Unitário']
    return df

df_vendas = carregar_dados()

st.title("Dashboard de vendas - Padaria do seu Zé")

categorias_selecionadas = st.sidebar.multiselect(label='Selecione as categorias:',
                        options=df_vendas['Categoria'].unique(),placeholder='Selecione')

forma_pagamento_selecionada = st.sidebar.multiselect(label='Selecione a Forma de Pagamento:',
                        options=df_vendas['Forma_Pagamento'].unique(),placeholder='Selecione')

data_inicio = st.sidebar.date_input(label='Data de inicío',
                    value=df_vendas['Data'].min())

data_final = st.sidebar.date_input(label='Data final',
                    value=df_vendas['Data'].max())

data_inicio = pd.to_datetime(data_inicio)
data_final = pd.to_datetime(data_final)

df_datas = (df_vendas['Data'] >= data_inicio) & (df_vendas['Data'] <= data_final) 
df_filtrado = df_vendas[df_datas]

if categorias_selecionadas:
    df_filtrado = df_filtrado[df_filtrado ['Categoria'].isin(categorias_selecionadas)]

if forma_pagamento_selecionada:
    df_filtrado = df_filtrado[df_filtrado['Forma_Pagamento'].isin(forma_pagamento_selecionada)]

total_vendas_filtrados = df_filtrado['total_vendas'].sum()
total_produtos_vendidos = df_filtrado['Quantidade'].sum()
try:
    ticket_medio = total_vendas_filtrados / len(df_filtrado)
except ZeroDivisionError:
    ticket_medio = 0

def formatar_numeros(numero):
    return (f'R${numero:,.2f}'
    .replace(',', '#')
    .replace('.', ',')
    .replace('#', '.')
)
vendas_formatado = formatar_numeros(total_vendas_filtrados)
ticket_formatado = f'R${ticket_medio:.2f}'.replace('.', ",")

vendas,ticket,total_produto = st.columns(3)

vendas.metric("Total de Vendas (R$)",value=vendas_formatado,border= True,)
ticket.metric("Valor médio de cada compra",value=ticket_formatado,border= True,)
total_produto.metric("Total de produtos vendidos",value=total_produtos_vendidos,border= True)

produtos_agrupados = df_filtrado.groupby("Produto")["Quantidade"].sum()
try:
    produto_mais_vendido = produtos_agrupados.idxmax()
except ValueError:
    produto_mais_vendido = "Nenhum produto"

st.metric(label="Produto mais vendido",value= produto_mais_vendido,border=True,width='stretch')

st.subheader("Total Vendido por categoria")

grafico_total = df_filtrado.groupby("Categoria")["total_vendas"].sum().reset_index()
grafico_total["total_formatado"] = grafico_total["total_vendas"].apply(formatar_numeros)
grafico_categorias = alt.Chart(grafico_total).mark_bar().encode(
    x=alt.X("Categoria", title="Categoria do produto"),
    y=alt.Y("total_vendas",title="Total Vendido(R$)"),
    tooltip=["Categoria","total_formatado"],
    color='Categoria'
).interactive()
st.altair_chart(grafico_categorias,use_container_width=True)

st.subheader("Vendas Por Data")
vendas_diarias = df_filtrado.groupby("Data")["total_vendas"].sum().reset_index()
grafico_diario = alt.Chart(vendas_diarias).mark_line(color='green').encode(
    x=alt.X("Data",title="Evolução diária de vendas"),
    y=alt.Y("total_vendas",title="Total Vendido (R$)"),
    tooltip=["Data","total_vendas"]
).interactive()
st.altair_chart(grafico_diario,use_container_width=True)

st.subheader("Venda total por Pagamento")
vendas_por_pagamento = df_filtrado.groupby("Forma_Pagamento")["total_vendas"].sum().reset_index()
vendas_por_pagamento['total_formatado'] = vendas_por_pagamento['total_vendas'].apply(formatar_numeros)
grafico_pagamento = alt.Chart(vendas_por_pagamento).mark_arc().encode(
    theta= alt.Theta("total_vendas",title="Total de vendas por pagamento"),
    tooltip=['Forma_Pagamento', "total_formatado"],
    color="Forma_Pagamento",
)
st.altair_chart(grafico_pagamento,use_container_width=True)

st.dataframe(df_filtrado)


csv_export = df_filtrado.to_csv(index=False)

st.download_button(label="Baixe a tabela filtrada aqui!", data=csv_export, file_name="vendas_filtradas.csv")


insta_url = "https://www.instagram.com/bernarrnarciso"
st.markdown(f"Desenvolvido com carinho. Me siga no Insta: [**bernarrnarciso**]({insta_url})")