def solution(numbers, target):
    global answer
    answer = 0
    
    def dfs(i, total) :
        global answer
        if (i == len(numbers)) :  # numbers 배열을 끝까지 탐색한 경우
            if total == target :  # 목표값과 같은 경우 answer 증가
                answer += 1
            return
        dfs(i + 1, total + numbers[i])    
        dfs(i + 1, total - numbers[i])
        return
    
    dfs(0, 0)
    return answer