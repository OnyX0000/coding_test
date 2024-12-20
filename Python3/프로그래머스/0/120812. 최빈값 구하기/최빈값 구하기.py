def solution(array):
    freq = {}
    for num in array :
        freq[num] = freq.get(num, 0) + 1

    max_count = max(freq.values())
    modes = [key for key, value in freq.items() if value == max_count]

    if len(modes) > 1 :
        return -1
    
    return modes[0]