from env.cliff_environment import CliffWalkingEnv
from agent.q_learning import QLearningAgent

env = CliffWalkingEnv()

n_states = env.row * env.col
n_actions = 4

agentQ = QLearningAgent(n_states, n_actions)

episodes = 500

# 优化参数设置
# epsilon_decay = 0.999
# epsilon_min = 0.01
# alpha_decay = 0.999
# alpha_min = 0.01

reward_avgQ = 0


count = 0

for episode in range(episodes):
    count += 1

    state = env.reset()
    done = False

    total_rewardQ = 0

    total_rewardQ = 0
    # agentQ.alpha = max(alpha_min, agentQ.alpha * alpha_decay)
    # 学习率衰减
    # agent.alpha = max(alpha_min, agent.alpha * alpha_decay)
    # agentQ.epsilon = max(epsilon_min, agentQ.epsilon * epsilon_decay)
    while not done:

        # Q_learning

        action = agentQ.choose_action(state)

        next_state, rewardQ, done = env.move(action)

        agentQ.update(state, action, rewardQ, next_state, done)

        state = next_state

        total_rewardQ += rewardQ

    print("episode:", episode, ", reward:", total_rewardQ)

    reward_avgQ += total_rewardQ

    if count == 500:
        with open("./rewardQ.txt", "a") as f:
            f.write(str(reward_avgQ/500) + "\n")
        reward_avgQ = 0
        count = 0
