def solution(numbers, hand):
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2), '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    left_thumb, right_thumb = '*', '#'
    result = ''

    for num in numbers :
        if num in [1, 4, 7] :
            result += 'L'
            left_thumb = num
        elif num in [3, 6, 9] :
            result += 'R'
            right_thumb = num
        else :
            left_dist = abs(keypad[left_thumb][0] - keypad[num][0]) + abs(keypad[left_thumb][1] - keypad[num][1])
            right_dist = abs(keypad[right_thumb][0] - keypad[num][0]) + abs(keypad[right_thumb][1] - keypad[num][1])
            if left_dist < right_dist or (left_dist == right_dist and hand == "left") :
                result += 'L'
                left_thumb = num
            else :
                result += 'R'
                right_thumb = num

    return result
