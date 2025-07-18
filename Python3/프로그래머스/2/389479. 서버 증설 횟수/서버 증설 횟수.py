def solution(players, m, k):
    import math
    
    n = 24
    operating = [0] * (n + k)  # 각 시각별 실제 운영 중인 서버 수
    answer = 0

    for i in range(n) :
        p = players[i]

        # 1. 이번 시간대에 필요한 추가 서버 수
        if p < m :
            required = 0
        else:
            required = (p - m) // m + 1

        # 2. 현재 운영 중인 서버 수
        running = operating[i]

        # 3. 부족하면 증설
        if required > running :
            need = required - running
            answer += need
            for t in range(i, i + k) :        # k시간 동안 가동
                operating[t] += need

    return answer
