import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import tensorflow as tf

# Dados fictícios de vendas ao longo do tempo
np.random.seed(42)
meses = np.arange(1, 13).reshape(-1, 1)  # formato coluna
vendas = np.array([200, 220, 250, 280, 300, 320, 350, 380, 400, 420, 450, 480])

# DataFrame
dados = pd.DataFrame({'Mes': meses.flatten(), 'Vendas': vendas})

# Visualizar dados
plt.scatter(dados['Mes'], dados['Vendas'])
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Dados de Vendas ao Longo do Tempo')
plt.show()

# Dividir em treino e teste
X = dados[['Mes']]
y = dados[['Vendas']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar X (apenas as features, não o alvo)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelo de regressão
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(units=8, activation='relu'),
    tf.keras.layers.Dense(units=1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Treinamento
model.fit(X_train_scaled, y_train, epochs=500, verbose=0)

# Previsões
predictions = model.predict(X_test_scaled)

# Avaliação
erro_mse = mean_squared_error(y_test, predictions)
print(f'Erro Médio Quadrático (MSE): {erro_mse:.2f}')

# Visualização
plt.scatter(X_test, y_test, label='Dados Reais')
plt.scatter(X_test, predictions, color='red', label='Previsões')
plt.xlabel('Mês')
plt.ylabel('Vendas')
plt.title('Previsões de Vendas com Regressão (TensorFlow)')
plt.legend()
plt.show()

# Previsão para o próximo mês
proximo_mes_scaled = scaler.transform(np.array([[13]]))
previsao_proximo_mes = model.predict(proximo_mes_scaled)[0, 0]
print(f'Previsão de Vendas para o Próximo Mês: {previsao_proximo_mes:.2f}')
