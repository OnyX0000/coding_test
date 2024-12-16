def solution(numbers):
    answer = 0
    temp = []
    while numbers :
        first = numbers[0]
        numbers.remove(first)
        for i in numbers :
            temp.append(first * i)
    return max(temp)