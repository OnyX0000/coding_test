def solution(n):
    temp = ''
    
    while n != 0 :
        temp += str(n % 3)
        n //= 3
    
    return int(temp, 3)