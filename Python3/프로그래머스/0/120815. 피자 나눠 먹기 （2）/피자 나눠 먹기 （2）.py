def solution(n):
    slices = 6
    pizzas = 1
    
    while (slices * pizzas) % n != 0 :
        pizzas += 1
    return pizzas