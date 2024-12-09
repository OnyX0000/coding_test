def solution(my_string, indices):
    answer = ''
    indices_set = set(indices)
    answer = [char for i, char in enumerate(my_string) if i not in indices_set]
    return ''.join(answer)
