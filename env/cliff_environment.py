import numpy as np


class CliffWalkingEnv:

    def __init__(self):
        """
        Cliff Walking Environment

        Grid size: 4 * 12

        S = Start
        G = Goal
        C = Cliff
        """

        self.row = 4
        self.col = 12

        self.start = (3, 0)
        self.goal = (3, 11)

        self.pos = self.start

        self.action = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        self.cliff = [(3, i) for i in range(1, 11)]

    def move(self, actions):
        """
        Let the model move and update its position 
        """

        x, y = self.pos
        dx, dy = self.action[actions]

        nx = x + dx
        ny = y + dy

        nx = max(0, min(self.row-1, nx))
        ny = max(0, min(self.col-1, ny))

        if (nx, ny) in self.cliff:
            reward = -100
            done = True

            self.pos = self.start

        elif (nx, ny) in self.goal:
            reward = 0
            done = True

        else:
            reward = -1
            done = False

        return self._get_state(), reward, done

    def reset(self):
        """
        Reset at every episode
        """

        self.pos = self.start

    def _get_state(self):
        """
        Change (x,y) into state index
        """

        x, y = self.pos
        return x * self.row + self.col

    def render(self):
        """
        Print the current environment
        """

        grid = [["." for _ in range(self.col)] for _ in range(self.row)]

        # cliff
        for x, y in self.cliff:
            grid[x][y] = "C"

        # Start and Goal
        sx, sy = self.start
        gx, gy = self.goal

        grid[sx][sy] = "S"
        grid[gx][gy] = "G"

        # agent
        ax, ay = self.pos
        grid[ax][ay] = "A"

        for row in grid:
            print(" ".join(row))

        print()
