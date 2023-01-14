import random
import two_arms_bandit

from scipy.stats import beta as Beta

def run(n, gamma, init_list) -> int:
    """传入拉动次数 n，初始化列表 init_list（必须包含两个元素以初始化两个摇杆的 alpha beta 值），返回结果"""

    ans = 0.0
    expect = [0.0 for _ in range(3)]
    alpha = [0.0 for _ in range(3)]
    beta = [0.0 for _ in range(3)]

    alpha[1], beta[1] = init_list[0], init_list[1]
    alpha[2], beta[2] = init_list[0], init_list[1]

    for t in range(1, n + 1):
        expect[1] = alpha[1] / (alpha[1] + beta[1])
        expect[2] = alpha[2] / (alpha[2] + beta[2])

        arm = expect.index(max(expect))

        tmp = two_arms_bandit.pull_arm(arm)

        ans += pow(gamma, t - 1)
        alpha[arm] += tmp
        beta[arm] += 1 - tmp

    return ans
