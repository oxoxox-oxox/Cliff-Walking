from env.cliff_environment import CliffWalkingEnv
from agent.q_learning import QLearningAgent

env = CliffWalkingEnv()

n_states = env.row * env.col
n_actions = 4

agent = QLearningAgent(n_states, n_actions)

episodes = 10000


# 优化参数设置
epsilon_decay = 0.95
epsilon_min = 0.01
alpha_decay = 0.99
alpha_min = 0.01


for episode in range(episodes):

    state = env.reset()
    done = False

    total_reward = 0

    while not done:
        # 学习率衰减
        agent.alpha = max(alpha_min, agent.alpha * alpha_decay)
        # 探索率衰减
        agent.epsilon = max(epsilon_min, agent.epsilon * epsilon_decay)

        action = agent.choose_action(state)

        next_state, reward, done = env.move(action)

        agent.update(state, action, reward, next_state)

        state = next_state

        total_reward += reward

        print("episode:", episode, ", reward:", total_reward)
