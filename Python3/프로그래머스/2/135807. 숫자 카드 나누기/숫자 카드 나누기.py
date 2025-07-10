from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    def get_gcd(arr):
        return reduce(gcd, arr)
    
    def is_valid(gcd_value, other_array):
        return all(x % gcd_value != 0 for x in other_array)
    
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)

    answer = 0
    if is_valid(gcdA, arrayB):
        answer = max(answer, gcdA)
    if is_valid(gcdB, arrayA):
        answer = max(answer, gcdB)
        
    return answer
