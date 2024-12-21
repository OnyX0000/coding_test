def solution(lines):
    line_map = [0] * 201  

    for start, end in lines :
        for i in range(start + 100, end + 100) :
            line_map[i] += 1

    return sum(1 for x in line_map if x > 1)
