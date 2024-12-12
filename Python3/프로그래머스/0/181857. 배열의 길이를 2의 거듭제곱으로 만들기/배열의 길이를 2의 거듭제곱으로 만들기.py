def solution(arr):
    answer = []
    if len(arr) == 0 :
        return []
    while len(arr) not in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] :
        arr.append(0)
    answer = arr
    return answer