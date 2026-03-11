# Cliff-Walking

This repository use reinforce learning to achieve Cliff Walking using Q-learning and Sarsa method

## The structure of the repository

```bash
project_root/
├── agent/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── q_learning.py
│   └── sarsa.py
├── env/
│   ├── __pycache__/
│   ├── __init__.py
│   └── cliff_environment.py
├── txt/                # 空目录（或未列出具体文件）
├── utils/
│   └── plot.py
├── .gitignore
├── main_q_learning.py
├── main_sarsa.py        # 注意：文件名可能为 main_sarsa.py 的笔误
└── README.md
```

## Function

This repository using Q-learning and Sarsa method to simulate the process of Robot walking through a cliff

After about 50000 episode, the robot will find the best solution to walk to the destination other than fall from cliff

## Process

The map in this repository is as follow:

```bash
0,0,0,0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0,0,0,0
0,0,0,0,0,0,0,0,0,0,0,0
S,C,C,C,C,C,C,C,C,C,C,G
```

Robot start from the "S" point, and the goal of the Robot is to reach the "G" point.

I set every point on the map a reward

|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|
|--|--|--|--|--|--|--|--|--|--|--|--|
|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|
|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|-1|
|-1| -100| -100| -100| -100| -100| -100| -100| -100| -100| -100| 0|

So if the robot walk to the cliff, it will gain great decrease in the reward

---

Finally, you can use plot.py in the utils folder to draw a graph to analyse the outcome

```bash
python ./utils/plot.py
```
