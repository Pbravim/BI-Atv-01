import pandas as pd
from IPython.display import display

# Carregando os dados dos arquivos CSV
fornecedores = pd.read_csv('Fornecedores.csv')
transportadoras = pd.read_csv('Transportadoras.csv')
vendas_globais = pd.read_csv('Vendas Globais.csv')
vendedores = pd.read_csv('Vendedores.csv')

# Juntando os DataFrames conforme necessário
dados = vendas_globais.merge(fornecedores, on='FornecedorID').merge(transportadoras, on='TransportadoraID').merge(vendedores, on='VendedorID')

# Convertendo coluna de datas para tipo datetime, se aplicável
dados['Data'] = pd.to_datetime(dados['Data'], format='%d/%m/%Y')


# 1. Quem são os meus 10 maiores clientes, em termos de vendas ($)?
top_10_clientes = dados.groupby('ClienteNome').sum(numeric_only=True).sort_values(by='Vendas', ascending=False).head(10)
top_10_clientes.reset_index(inplace=True)
top10_cliente_display = top_10_clientes[["ClienteNome", "Vendas"]]
print("-----------------1--------------------")
display(top10_cliente_display)

# 2. Quais os três maiores países, em termos de vendas ($)?
top_3_paises = dados.groupby('ClientePaís').sum(numeric_only=True).sort_values(by='Vendas', ascending=False).head(3)
top_3_paises.reset_index(inplace=True)
top_3_paises_display = top_3_paises[["ClientePaís", "Vendas"]]
print("-----------------2--------------------")
display(top_3_paises_display)

# 3. Quais as categorias de produtos que geram maior faturamento (vendas $) no Brasil?
categorias_brasil = dados[dados['ClientePaís'] == 'Brazil'].groupby('CategoriaDescrição').sum(numeric_only=True).sort_values(by='Vendas', ascending=False)
categorias_brasil.reset_index(inplace=True)
categorias_brasil_display = categorias_brasil[["CategoriaDescrição", "Vendas"]]
print("-----------------3--------------------")
display(categorias_brasil_display)

# 4. Qual a despesa com frete envolvendo cada transportadora?
despesa_frete = dados.groupby('TransportadoraNome')['Frete'].sum().sort_values(ascending=False)
print("-----------------4--------------------")
display(despesa_frete)

# 5. Quais são os principais clientes (vendas $) do segmento “Calçados Masculinos” (Men's Footwear) na Alemanha?
clientes_calcados_alemanha = dados[(dados['CategoriaNome'] == "Men´s Footwear") & (dados['ClientePaís'] == 'Germany')].groupby('ClienteNome').sum(numeric_only=True).sort_values(by='Vendas', ascending=False)
print('----------------5---------------------')
clientes_calcados_alemanha.reset_index(inplace=True)
cliente_calcados_display = clientes_calcados_alemanha[['ClienteNome', 'Vendas']]
display(cliente_calcados_display)

# 6. Quais os vendedores que mais dão descontos nos Estados Unidos?
vendedores_descontos_usa = dados[dados['ClientePaís'] == 'USA'].groupby('VendedorNome')['Desconto'].sum().sort_values(ascending=False)
print("-------------6------------------------")
# vendedores_descontos_usa.reset_index(inplace=True)
# vendedores_usa_display = vendedores_descontos_usa[['VendendorNome', 'Desconto']]
display(vendedores_descontos_usa)

# 7. Quais os fornecedores que dão a maior margem de lucro ($) no segmento de “Vestuário Feminino” (Women's Wear)?
fornecedores_margem_vestuario_feminino = dados[dados['CategoriaNome'] == 'Womens wear'].groupby('FornecedorNome')['Margem Bruta'].sum().sort_values(ascending=False)
print("---------------7----------------------")
display(fornecedores_margem_vestuario_feminino)


# 8. Quanto que foi vendido ($) no ano de 2009?
vendas_2009 = dados[dados['Data'].dt.year == 2009]['Vendas'].sum()
vendas_anuais = dados.groupby(dados['Data'].dt.year)['Vendas'].sum()
print("-----------------8--------------------")
display(vendas_2009)
print("-------------------------------------Vendas Anuais---------------------------")
display(vendas_anuais)

# 9. Quais são os principais clientes (vendas $) do segmento “Calçados Masculinos” (Men's Footwear) na Alemanha?
# IGUAL A QUESTÃO 5
# clientes_calcados_alemanha = dados[(dados['CategoriaNome'] == "Men´s Footwear") & (dados['ClientePaís'] == 'Alemanha')].groupby('ClienteNome').sum().sort_values(by='Vendas', ascending=False)
# print("----------------9---------------------")
# print(clientes_calcados_alemanha)

# 10. Quais os países nos quais mais se tiram pedidos (quantidade total de pedidos)?
pedidos_por_pais = dados['ClientePaís'].value_counts()
print("-----------------10--------------------")
display(pedidos_por_pais)
print("-------------------------------------")

