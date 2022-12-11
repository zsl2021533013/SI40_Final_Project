import math
import bandit


def run(n, c) -> int:
    """传入拉动次数 n，常数 c，返回结果"""

    ans = 0
    theta = [0.0 for _ in range(4)]
    count = [1 for _ in range(4)]  # 一开始都运行了一次

    theta[0] = float("-inf")
    theta[1] = bandit.pull_arm(1)
    theta[2] = bandit.pull_arm(2)
    theta[3] = bandit.pull_arm(3)

    for t in range(4, n + 1):
        tmp = theta
        for j in range(1, 4):
            tmp[j] += c * math.sqrt((2 * math.log2(t)) / count[j])
        arm = tmp.index(max(tmp))

        tmp = bandit.pull_arm(arm)

        ans += tmp
        count[arm] += 1
        theta[arm] += (tmp - theta[arm]) / count[arm]

    return ans
