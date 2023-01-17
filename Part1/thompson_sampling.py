import random

import numpy as np

import bandit

from scipy.stats import beta as Beta


def run(n, init_list) -> int:
    """传入拉动次数 n，初始化列表 init_list（必须包含六个元素以初始化三个摇杆的 alpha beta 值），返回结果"""

    ans = 0
    theta = [0.0 for _ in range(4)]
    alpha = [0.0 for _ in range(4)]
    beta = [0.0 for _ in range(4)]

    theta[0] = float("-inf")
    alpha[1], beta[1] = init_list[0], init_list[1]
    alpha[2], beta[2] = init_list[2], init_list[3]
    alpha[3], beta[3] = init_list[4], init_list[5]

    for t in range(1, n + 1):
        for j in range(1, 4):
            theta[j] = np.random.beta(alpha[j], beta[j])
        arm = np.argmax(theta)

        tmp = bandit.pull_arm_dependent(arm)

        ans += tmp
        alpha[arm] += tmp
        beta[arm] += 1 - tmp

    return ans