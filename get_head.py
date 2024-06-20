def probability_of_heads(n, k, p):
    DP = [[0] * (k + 1) for _ in range(n + 1)]
    DP[0][0] = 1

    for i in range(1, n + 1):
        for j in range(k + 1):
            prob_heads = 0
            for l in range(min(j, i) + 1):
                prob_heads += DP[i - 1][j - l] * p[i - 1] if l <= j else 0
            DP[i][j] = prob_heads

    return DP[n][k]

# Example usage:
n = 3
k = 2
p = [0.3, 0.5, 0.7]
print(probability_of_heads(n, k, p))  # Output: Probability of getting exactly 2 heads when tossing 3 biased coins
