# Cliff-Walking

This repository implements the Cliff Walking problem using reinforcement learning algorithms: Q-learning and Sarsa methods.

## Repository Structure

```bash
project_root/
├── agent/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── q_learning.py        # Q-learning algorithm implementation
│   └── sarsa.py             # Sarsa algorithm implementation
├── env/
│   ├── __pycache__/
│   ├── __init__.py
│   └── cliff_environment.py # Cliff environment implementation
├── utils/
│   └── plot.py              # Reward visualization tool
├── .gitignore
├── main_q_learning.py       # Main script for Q-learning
├── main_sarsa.py            # Main script for Sarsa
├── rewardQ.txt              # Q-learning reward data
├── rewardS.txt              # Sarsa reward data
├── requirements.txt         # Python dependencies
└── README.md
```

## Overview

This project simulates a robot navigating through a cliff environment using two reinforcement learning algorithms:

- **Q-learning**: An off-policy algorithm that learns the optimal policy by estimating the Q-values for state-action pairs
- **Sarsa**: An on-policy algorithm that learns while following the current policy

## Environment

The cliff environment is represented as a 4x12 grid:

```
0,0,0,0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0,0,0,0
S,C,C,C,C,C,C,C,C,C,C,G
```

- **S**: Start position (bottom-left corner)
- **G**: Goal position (bottom-right corner)
- **C**: Cliff positions (falling off results in a large negative reward)

### Reward Structure

| -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
|----|----|----|----|----|----|----|----|----|----|----|----|
| -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
| -1 | -100| -100| -100| -100| -100| -100| -100| -100| -100| -100| 0 |

- Each step incurs a reward of -1
- Falling off the cliff (stepping on 'C') incurs a reward of -100
- Reaching the goal ('G') incurs a reward of 0

## How to Run

### 1. Run Q-learning

```bash
python main_q_learning.py
```

### 2. Run Sarsa

```bash
python main_sarsa.py
```

### 3. Visualize Results

After running the algorithms, you can visualize the reward convergence using the plot tool:

```bash
python utils/plot.py
```

## Expected Behavior

After approximately 50,000 episodes, both algorithms should converge to an optimal policy that navigates from the start to the goal while avoiding the cliff.

## Key Differences Between Q-learning and Sarsa

- **Q-learning** tends to find the optimal path that maximizes reward, which may involve taking more risks
- **Sarsa** tends to find a safer path that avoids potential dangers, even if it's slightly longer

This difference in behavior is often referred to as the "exploration-exploitation" trade-off in reinforcement learning.

## Dependencies

- Python 3.x
- NumPy (for numerical operations)
- Matplotlib (for visualization)
