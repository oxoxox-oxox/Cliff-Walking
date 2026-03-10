import matplotlib.pyplot as plt

rewards = []

# 假设训练时记录reward
with open("reward.txt") as f:
    for line in f:
        rewards.append(float(line.strip()))

plt.figure()
plt.plot(rewards)

plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Training Reward Curve")

plt.show()
