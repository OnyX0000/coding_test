def solution(arr, k):
    answer = []  
    seen = set()  

    for num in arr:
        if num not in seen:  
            answer.append(num)  
            seen.add(num)  
            
        if len(answer) == k: 
            break

    while len(answer) < k:
        answer.append(-1)

    return answer