import intutive_algorithm

dp = [[[[-1 for _ in range(100)] for _ in range(100)] for _ in range(100)] for _ in range(100)]

def R(n, gamma, depth, alpha1, beta1, alpha2, beta2) -> float:
    if depth == n:
        return 0
    if dp[alpha1][beta1][alpha2][beta2] > -1:
        return dp[alpha1][beta1][alpha2][beta2]

    R_1 = alpha1 / (alpha1 + beta1) * (1 + gamma * R(n, gamma, depth + 1, alpha1 + 1, beta1, alpha2, beta2)) + \
          beta1 / (alpha1 + beta1) * (1 + gamma * R(n, gamma, depth + 1, alpha1, beta1 + 1, alpha2, beta2))
    R_2 = alpha2 / (alpha2 + beta2) * (1 + gamma * R(n, gamma, depth + 1, alpha1, beta1, alpha2 + 1, beta2)) + \
          beta2 / (alpha2 + beta2) * (1 + gamma * R(n, gamma, depth + 1, alpha1, beta1, alpha2, beta2 + 1))

    dp[alpha1][beta1][alpha2][beta2] = max(R_1, R_2)

    return dp[alpha1][beta1][alpha2][beta2]

ans = intutive_algorithm.run(10, 0.9, [1, 1, 1, 1])

print(ans)