def solution(s):
    temp = s.lower()
    return True if temp.count('p') == temp.count('y') else False