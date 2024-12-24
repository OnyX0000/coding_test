def solution(price, money, count):
    temp = 0
    for i in range(1, count + 1) :
        temp += price * i 
    return 0 if money >= temp else abs(money - temp)