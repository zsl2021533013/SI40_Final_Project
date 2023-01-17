import numpy as np
import matplotlib.pyplot as plt
import epsilon_greedy
import thompson_sampling
import ucb_algorithm
import bandit

n = 5000
loop_time = 10
point_num = 10

ans = [0 for _ in range(point_num)]
for i in range(0, loop_time):
    ans[1] += epsilon_greedy.run(n, 0.1)
    ans[2] += epsilon_greedy.run(n, 0.5)

print(ans[1] / (loop_time * n))
print(ans[2] / (loop_time * n))
