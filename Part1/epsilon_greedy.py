import random
import bandit


def run(n, epsilon) -> int:
    """传入拉动次数 n，常数 epsilon，返回结果"""

    ans = 0
    theta = [0.0 for _ in range(4)]
    count = [0 for _ in range(4)]

    theta[0] = float("-inf")

    for t in range(1, n + 1):
        tmp = random.random()
        if tmp < epsilon:
            arm = random.randint(1, 3)
        else:
            arm = theta.index(max(theta))

        tmp = bandit.pull_arm(arm)

        ans += tmp
        count[arm] += 1
        theta[arm] += (tmp - theta[arm]) / count[arm]

    return ans
