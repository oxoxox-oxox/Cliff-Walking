from env.cliff_environment import CliffWalkingEnv
from agent.sarsa import Sarsa

env = CliffWalkingEnv()

n_states = env.row * env.col
n_actions = 4

agentS = Sarsa(n_states, n_actions)

episodes = 1000


# 优化参数设置
epsilon_decay = 0.999
epsilon_min = 0.1
# alpha_decay = 0.9999
# alpha_min = 0.01

reward_avgS = 0


count = 0

for episode in range(episodes):
    count += 1

    state = env.reset()
    done = False

    action = agentS.choose_action(state)

    total_rewardS = 0

    # 学习率衰减
    # agent.alpha = max(alpha_min, agent.alpha * alpha_decay)
    # 探索率衰减
    agentS.epsilon = max(epsilon_min, agentS.epsilon * epsilon_decay)

    while not done:

        # Q_learning

        next_state, rewardS, done = env.move(action)

        next_action = agentS.choose_action(next_state)

        agentS.update(state, action, rewardS, next_state, done, next_action)

        state = next_state

        total_rewardS += rewardS

        action = next_action

    print("episode:", episode, ", reward:", total_rewardS)

    reward_avgS += total_rewardS

    if count == 500:
        with open("./rewardS.txt", "a") as f:
            f.write(str(reward_avgS/500) + "\n")
        reward_avgS = 0
        count = 0
