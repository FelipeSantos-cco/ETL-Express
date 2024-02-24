import pandas as pd

df = pd.read_excel('../teste.xlsx')

for i in range(len(df.columns)):
    nome_coluna = df.columns[i]
    valores_coluna = df.iloc[:, i]

    print(f'{nome_coluna:<20}')
    print(f'{valores_coluna}')