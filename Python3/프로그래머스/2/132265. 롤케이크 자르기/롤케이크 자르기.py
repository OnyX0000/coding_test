def solution(topping):
    count = 0
    left = set()
    right = {}
    
    for i in topping :
        right[str(i)] = right.get(str(i), 0)
        right[str(i)] += 1
        
    for i in topping :
        left.add(i)
        right[str(i)] -= 1
        
        if right[str(i)] == 0 :
            del right[str(i)]
        if len(left) == len(right.keys()) :
            count += 1
        
    return count