import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt

#Dados de exemplo
X_unsupervised = tf.constant([[1.0, 2.0],
                              [2.0, 3.0],
                              [3.0, 4.0],
                              [4.0, 5.0]])

#Modelo Autoencoder Simples
input_layer = Input(shape=(2,))
encoded = Dense(units=1)(input_layer)   

autoencoder = Model(inputs=input_layer, outputs=decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

#treinamento do modelo não supervisionado
autoencoder.fit(X_unsupervised, X_unsupervised, epochs=1000, verbose=0)

#Previsão (reconstrução dos dados)
prediction_unsupervised = autoencoder.predict(X_unsupervised)
print("Predição Não Supervisionada:", prediction_unsupervised)

#Visualização dos dados originais vs reconstruídos
plt.scatter(X_unsupervised[:, 0], X_unsupervised[:, 1], label="Original", c="blue", s=100)
plt.scatter(prediction_unsupervised[:, 0], prediction_unsupervised[:, 1], label="Reconstruído", c="red", marker="x", s=100)

plt.xlabel("Dimensão 1")
plt.ylabel("Dimensão 2")
plt.legend()
plt.title("Autoencoder - Dados Originais vs Reconstruídos")
plt.show()
