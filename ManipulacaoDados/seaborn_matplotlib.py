import seaborn as sns
import matplotlib.pyplot as plt

#Estilo
sns.set(style="whitegrid")  # opções: darkgrid, whitegrid, dark, white, ticks

#Dataset exemplo do seaborn
df_tips = sns.load_dataset('tips')

#Criar a figura com 3 subplots
fig, ax = plt.subplots(1, 3, figsize=(15, 5))

#Média por sexo
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])

#Soma por sexo
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)

#Contagem de registros por sexo
sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=lambda x: len(x))

plt.show()
