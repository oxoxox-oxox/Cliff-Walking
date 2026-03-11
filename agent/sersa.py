import numpy as np
import random


class Sersa:

    def __init__(self, n_states, n_actions):

        self.q_table = np.zeros((n_states, n_actions))

        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 1.0

        self.n_actions = n_actions

    def choose_action(self, state):

        # epsilon-greedy
        if random.random() < self.epsilon:
            return random.randint(0, self.n_actions - 1)

        return np.argmax(self.q_table[state])

    def update(self, s, a, r, s_next, done):

        best_next = np.max(self.q_table[s_next])

        td_target = r + self.gamma * self.q_table[s_next][next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += alpha * td_error

        self.q_table[s, a] += self.alpha * td_error
