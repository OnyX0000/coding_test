def solution(n):
    i = n + 1
    while True : 
        if str(bin(i)).count('1') == str(bin(n)).count('1') :
            return i
        else :
            i += 1