import matplotlib.pyplot as plt

# 读取 Q-learning 的奖励数据
rewardsQ = []
with open("./rewardQ.txt", "r") as f:
    for line in f:
        rewardsQ.append(float(line.strip()))

# 读取 Sarsa 的奖励数据
rewardsS = []
with open("./rewardS.txt", "r") as f:
    for line in f:
        rewardsS.append(float(line.strip()))

rewardsDQ = []
with open("./rewardDQ.txt", "r") as f:
    for line in f:
        rewardsDQ.append(float(line.strip()))


plt.figure(figsize=(10, 6))
plt.plot(rewardsQ, label='Q-learning', color='blue', linestyle='-')
plt.plot(rewardsS, label='Sarsa', color='red', linestyle='--')
plt.plot(rewardsDQ, label='Dyna-Q', color='yellow', linestyle='-.')

plt.xlabel("Episode (x10)")          # 因为每500个episode记录一次平均值
plt.ylabel("Average Reward")
plt.title("Comparison of Q-learning and Sarsa Training Rewards")
plt.legend()                           # 显示图例
plt.grid(True, alpha=0.3)               # 添加网格线，更易读
plt.show()
