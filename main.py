from env.cliff_environment import CliffWalkingEnv
from agent.q_learning import QLearningAgent

env = CliffWalkingEnv()

n_states = env.row * env.col
n_actions = 4

agent = QLearningAgent(n_states, n_actions)

episodes = 500

for episode in range(episodes):

    state = env.reset()
    done = False

    total_reward = 0

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.move(action)

        agent.update(state, action, reward, next_state)

        state = next_state

        total_reward += reward

    print("episode", episode, "reward", total_reward)
