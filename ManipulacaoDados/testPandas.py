import pandas as pd

data = {
    "Nome |" : ['Produto A', 'Produto B', 'Produto C', 'Produto A', 'Produto E',
                'Produto F', 'Produto G', 'Produto H', 'Produto I', 'Produto J'],
    "Quantidade de itens comprados |": [3, 1, 4, 3, 2, 5, 2, 6, 1, 3],
    "Tipo de item |" : ['Eletronico', 'Vestuario', 'Alimento', 'Eletronico', 'Alimento',
                        'Eletronico', 'Vestuario', 'Alimento', 'Eletronico', 'Vestuario'],
    "Receita total |" : [120, 80, 60, 120, 90, 200, 150, 300, 90, 120]
}
df = pd.DataFrame(data)
print(df)

#Remover itens duplicados
print("")
df.drop_duplicates(keep='last', inplace=True)
print(df)

#Calculando a coluna 'Preço do item'
df["Preço do item |"] = df ["Receita total |"] / df["Quantidade de itens comprados |"]

#Valor total da receita acumulada:
print("")
print(" ~~ Valor total acumulado ~~ ".center(50))
receita_total_acumulada = df['Receita total |'].sum()
print(f"{receita_total_acumulada}".center(50))

#Produto mais vendido
print("")
print(" ~~ Produto mais vendido ~~".center(50))
produtos_mais_vendidos = df.groupby("Nome |")['Quantidade de itens comprados |'].sum().idxmax()
quantidade = df.groupby("Nome |")['Quantidade de itens comprados |'].sum().max()
print(f"{produtos_mais_vendidos} com {quantidade} itens vendidos".center(50))

#Menor e maior preço encontrado na lista
print("")
print(" ~~ Preço minimo e máximo ~~".center(50))
preco_minimo = df["Preço do item |"].min()
preco_maximo = df["Preço do item |"].max()
print(f"Preço minimo: {preco_minimo:.2f}".center(50))
print(f"Preço maximo: {preco_maximo:.2f}".center(50))