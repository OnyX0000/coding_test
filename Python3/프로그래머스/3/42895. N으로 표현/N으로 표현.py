def solution(N, number):
    if N == number :
        return 1  # N이 number라면 최소 횟수는 1
    
    dp = [set() for _ in range(9)]  # dp[i]: N을 i번 사용하여 만들 수 있는 숫자들
    
    for i in range(1, 9) :  # N 사용 횟수 (1 ~ 8)
        dp[i].add(int(str(N) * i))  # N, NN, NNN, ... 
        
        for j in range(1, i) :
            for num1 in dp[j] :  # 앞
                for num2 in dp[i - j] :  # 뒷
                    dp[i].add(num1 + num2)  # +
                    dp[i].add(num1 - num2)  # -
                    dp[i].add(num1 * num2)  # *
                    if num2 != 0 :
                        dp[i].add(num1 // num2)  # // 나머지 무시
        
        if number in dp[i] :  # 목표 숫자가 포함된 경우
            return i

    return -1  # 8번을 넘어서면 -1 반환