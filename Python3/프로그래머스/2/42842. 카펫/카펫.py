def solution(brown, yellow):  
    x= 0.5 * ((2 + brown / 2) + ((2 + brown / 2) * (2 + brown / 2) - 4 * brown - 4 * yellow) ** 0.5)
    y= 0.5 * brown - x + 2
        
    return [x, y]
