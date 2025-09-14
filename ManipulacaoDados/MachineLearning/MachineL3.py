import tensorflow as tf
import gym
import numpy as np

# Ambiente CartPole do Gym
env = gym.make("CartPole-v1")

# Modelo Simples (Q-network)
model_reinforcement = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation="relu", input_shape=(env.observation_space.shape[0],)),
    tf.keras.layers.Dense(env.action_space.n, activation="linear")
])

model_reinforcement.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss="mse")

# Hiperparâmetros
gamma = 0.95
epsilon = 1.0   # Exploração
epsilon_decay = 0.995
epsilon_min = 0.01
max_episodes = 200

# Treinamento
for episode in range(max_episodes):
    state, _ = env.reset()
    state = np.reshape(state, [1, env.observation_space.shape[0]])
    total_reward = 0
    done = False

    while not done:
        # Escolher ação (exploração vs exploração)
        if np.random.rand() <= epsilon:
            action = env.action_space.sample()
        else:
            q_values = model_reinforcement.predict(state, verbose=0)
            action = np.argmax(q_values[0])

        # Executar ação
        next_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated
        next_state = np.reshape(next_state, [1, env.observation_space.shape[0]])
        total_reward += reward

        # Atualizar Q-target
        target = reward
        if not done:
            target += gamma * np.amax(model_reinforcement.predict(next_state, verbose=0)[0])

        target_f = model_reinforcement.predict(state, verbose=0)
        target_f[0][action] = target

        # Treinar rede
        model_reinforcement.fit(state, target_f, epochs=1, verbose=0)

        state = next_state

    # Decaimento do epsilon
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    # Feedback
    print(f"Episode {episode+1}/{max_episodes}, Reward: {total_reward}, Epsilon: {epsilon:.3f}")
