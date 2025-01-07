def solution(s):
    cnt, zero = 0, 0
    
    while s != '1' :
        zero += s.count('0')
        s = bin(s.count('1'))[2:]
        cnt += 1

    return [cnt, zero]