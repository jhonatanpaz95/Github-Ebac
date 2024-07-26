# código de geração do gráfico 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='dia', y='venda')
plt.title("Preço de venda da Gasolina")
plt.xlabel("Dia")
plt.ylabel("Preço")
plt.show()
plt.savefig('gasolina.png')