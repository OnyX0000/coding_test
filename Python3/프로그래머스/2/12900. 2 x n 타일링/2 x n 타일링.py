def solution(n):
    MOD = 1_000_000_007
    a, b = 1, 1  # dp[0], dp[1]
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD
    return b
