def solution(s):
    elements = s.split()
    temp = []

    for element in elements :
        if element == "Z" :
            if temp :  
                temp.pop() 
        else:
            temp.append(int(element))  

    return sum(temp)