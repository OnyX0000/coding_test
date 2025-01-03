def solution(board, moves):
    basket = []
    answer = 0

    for move in moves :
        for row in board :
            if row[move - 1] != 0 :
                doll = row[move - 1]
                row[move - 1] = 0
                if basket and basket[-1] == doll :
                    basket.pop()
                    answer += 2
                else :
                    basket.append(doll)
                break

    return answer