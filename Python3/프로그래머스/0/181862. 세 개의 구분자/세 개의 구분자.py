def solution(myStr):
    answer = []
    split = myStr.split('a')
    temp = []
    for segment in split:
        temp.extend(segment.split('b'))
    for segment in temp:
        answer.extend(segment.split('c'))

    answer = [segment for segment in answer if segment]

    return answer if answer else ["EMPTY"]