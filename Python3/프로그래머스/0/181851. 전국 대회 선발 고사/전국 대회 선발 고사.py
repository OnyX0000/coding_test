def solution(rank, attendance):
    answer = 0
    dic = dict()
    prz = []
    
    for i in range(len(rank)) :
        dic[i] = [rank[i], attendance[i]]
        
    for i in dic.items() :
        if i[1][1] == True :
            prz.append((i[0], i[1][0]))
    prz = sorted(prz, key = lambda x : x[1])
    answer = 10000 * prz[0][0] + 100 * prz[1][0] + prz[2][0]
    return answer