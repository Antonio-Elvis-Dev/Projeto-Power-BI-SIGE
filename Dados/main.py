import pandas as pd

# Carregar os arquivos CSV ignorando as linhas problemáticas
df_2022 = pd.read_csv('2022_Pagamento.csv', encoding='ISO-8859-1', on_bad_lines='skip')
df_2023 = pd.read_csv('2023_Pagamento.csv', encoding='ISO-8859-1', on_bad_lines='skip')

# # Unir os DataFrames
# df_unido = pd.concat([df_2022, df_2023])

# # Salvar o DataFrame unido em um novo arquivo CSV
# df_unido.to_csv('pagamentos.csv', index=False, encoding='ISO-8859-1')

# print("Arquivo 'pagamentos.csv' salvo com sucesso!")


print(df_2022)
