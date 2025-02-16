def solution(m, n, puddles):
    mod = 1_000_000_007  # 결과를 나눌 값

    # DP 테이블 초기화 (모두 0으로 설정)
    dp = [[0] * m for _ in range(n)]

    # 물에 잠긴 지역 표시 (0,0) 기준으로 변환
    for x, y in puddles :
        dp[y - 1][x - 1] = -1  # 물에 잠긴 곳은 -1로 설정

    # 시작 위치 초기화
    dp[0][0] = 1  

    # DP 테이블 채우기
    for i in range(n) :
        for j in range(m) :
            if dp[i][j] == -1 :  # 물에 잠긴 곳은 -1
                dp[i][j] = 0
                continue

            if i > 0 :  # 위쪽에서 오는 경로
                dp[i][j] += dp[i - 1][j] % mod

            if j > 0 :  # 왼쪽에서 오는 경로
                dp[i][j] += dp[i][j - 1] % mod

            dp[i][j] %= mod  # 값이 너무 커지는 것을 방지

    return dp[n - 1][m - 1]  # (m, n) 위치의 경로 개수 반환
