from env.cliff_environment import CliffWalkingEnv
from agent.q_learning import QLearningAgent

env = CliffWalkingEnv()

n_states = env.row * env.col
n_actions = 4

agent = QLearningAgent(n_states, n_actions)

episodes = 50000


# 优化参数设置
epsilon_decay = 0.999
epsilon_min = 0.1
# alpha_decay = 0.9999
# alpha_min = 0.01

reward_avg = 0


count = 0

for episode in range(episodes):
    count += 1

    state = env.reset()
    done = False

    total_reward = 0

    # 学习率衰减
    # agent.alpha = max(alpha_min, agent.alpha * alpha_decay)
    # 探索率衰减
    agent.epsilon = max(epsilon_min, agent.epsilon * epsilon_decay)

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.move(action)

        agent.update(state, action, reward, next_state, done)

        state = next_state

        total_reward += reward

    print("episode:", episode, ", reward:", total_reward)

    reward_avg += total_reward

    if count == 500:
        with open("./reward.txt", "a") as f:
            f.write(str(reward_avg/500) + "\n")
        reward_avg = 0
        count = 0
