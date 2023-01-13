import epsilon_greedy
import thompson_sampling_algorithm
import ucb_algorithm
import bandit

# n = 5000
# loop_time = 200
#
# ans = [0 for _ in range(4)]
# for i in range(loop_time):
#     ans[1] += epsilon_greedy.run(n, 0.1) / n
#     ans[2] += ucb_algorithm.run(n, 1) / n
#     ans[3] += thompson_sampling_algorithm.run(n, [601, 401, 401, 601, 2, 3]) / n
#
# print(ans[1] / loop_time)
# print(ans[2] / loop_time)
# print(ans[3] / loop_time)

print(bandit.pull_arm_dependent(1))
print(bandit.pull_arm_dependent(1))
print(bandit.pull_arm_dependent(2))
print(bandit.pull_arm_dependent(2))
print(bandit.pull_arm_dependent(2))