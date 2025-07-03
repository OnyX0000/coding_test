def solution(storey):
    answer = 0
    while storey > 0 :
        current_digit = storey % 10

        if current_digit > 5 :
            answer += 10 - current_digit
            storey += 10
        elif current_digit < 5 :
            answer += current_digit
        else :  # current_digit == 5
            if (storey // 10) % 10 >= 5 :
                answer += 5
                storey += 10
            else :
                answer += 5

        storey //= 10

    return answer
