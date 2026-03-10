from env import cliff_environment
from agent import q_learning

env = cliff_environment()

n_states = env.row * env.col
n_actions = 4

agent = q_learning(n_states, n_actions)

episodes = 500

for episode in range(episodes):

    state = env.reset()
    done = False

    total_reward = 0

    while not done:

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        agent.update(state, action, reward, next_state)

        state = next_state

        total_reward += reward

    print("episode", episode, "reward", total_reward)
