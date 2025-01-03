def solution(ingredient):
    answer = 0
    hamburger = [1, 2, 3, 1]
    temp = []
         
    for i in ingredient :
        temp.append(i)
        if len(temp) < 4 :
            continue
        else :
            if temp[-4:] == hamburger :
                answer += 1
                del temp[-4:]
            
    return answer