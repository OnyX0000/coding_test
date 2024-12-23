def solution(num):
    temp = 0
    if num == 1 :
        return 0
    while num != 1 :
        if num % 2 == 0 :
            num /= 2
        else : 
            num = num * 3 + 1
        temp += 1
        
    return temp if temp < 500 else -1