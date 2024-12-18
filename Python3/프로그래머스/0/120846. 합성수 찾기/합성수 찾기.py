def solution(n):
    c_count = 0
    
    for num in range(1, n + 1) :
        count = 0
        for i in range(1, num + 1) :
            if num % i == 0 :
                count += 1
            if count > 2 :
                c_count += 1
                break

    return c_count