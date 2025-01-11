def solution(arr):
    result = arr[0]
    for num in arr[1:] :
        a, b = result, num
        while b :
            a, b = b, a % b
        result *= num // a
    return result