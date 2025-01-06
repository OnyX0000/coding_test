def solution(s):
    # s를 int형 데이터들의 리스트로 분할
    s = list(map(int, s.split(" ")))
    return f'{min(s)} {max(s)}'