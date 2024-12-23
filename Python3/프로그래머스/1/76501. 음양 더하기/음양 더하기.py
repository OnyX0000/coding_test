def solution(absolutes, signs):
    temp = []
    for i in range(len(absolutes)) :
        if signs[i] :
            temp.append(absolutes[i])
        else :
            temp.append(-absolutes[i])
    return sum(int(j) for j in temp)