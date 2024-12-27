def solution(k, tangerine):
    size_counts = {}
    
    for size in tangerine :
        if size in size_counts :
            size_counts[size] += 1
        else:
            size_counts[size] = 1
    
    sorted_counts = sorted(size_counts.values(), reverse = True)
    
    total = 0
    answer = 0
    
    for count in sorted_counts :
        total += count
        answer += 1
        if total >= k :  
            break
    
    return answer