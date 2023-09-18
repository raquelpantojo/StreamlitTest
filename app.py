import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# importando os dados
dados = pd.read_csv('estoque.csv')

st.title('Análise de estoque\n')
st.write('Nesse projeto vamos analisar a quantidade de produtos em estoque, por categoria, de uma base de dados de produtos de supermercado')


# filtros para a tabela
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
if checkbox_mostrar_tabela:

    st.sidebar.markdown('## Filtro para a tabela')

    categorias = list(dados['Categoria'].unique())
    categorias.append('Todas')
    categoria = st.sidebar.selectbox('Selecione a categoria para apresentar na tabela', options = categorias)

    if categoria != 'Todas':
        df_categoria = dados.query('Categoria == @categoria')
        mostra_qntd_linhas(df_categoria)      
    else:
        mostra_qntd_linhas(dados)
        
        
        # função para selecionar a quantidade de linhas do dataframe
def mostra_qntd_linhas(dataframe):

    qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)

    st.write(dataframe.head(qntd_linhas).style.format(subset = ['Valor'], formatter="{:.2f}"))
    
    
    # filtro para o gráfico
st.sidebar.markdown('## Filtro para o gráfico')

categoria_grafico = st.sidebar.selectbox('Selecione a categoria para apresentar no gráfico', options = dados['Categoria'].unique())
figura = plot_estoque(dados, categoria_grafico)
st.pyplot(figura)
