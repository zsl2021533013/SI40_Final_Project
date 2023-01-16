import epsilon_greedy
import thompson_sampling
import ucb_algorithm
import bandit

n = 5000
loop_time = 200

ans = [0 for _ in range(4)]
for i in range(loop_time):
    ans[1] += thompson_sampling.run(n, [1, 1, 1, 1, 1, 1])
    ans[2] += thompson_sampling.run(n, [601, 401, 401, 601, 2, 3])

print(ans[1] / (loop_time * n))
print(ans[2] / (loop_time * n))
