def solution(want, number, discount):
    answer = 0
    want_dict = {}
    
    for i in range(len(discount) - 9) :
        temp = discount[i:i + 10]
        flag = 0
        for j in range(len(want)) :
            if temp.count(want[j]) != number[j] :
                flag = 1
                break
        if flag == 0 :
            answer += 1

    return answer
