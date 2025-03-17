def solution(order):
    stack = []
    length = len(order)
    answer = 0
    
    for num in range(1, length + 1) :
        stack.append(num)
        while stack and stack[-1] == order[answer]: 
            stack.pop()
            answer += 1

    return answer