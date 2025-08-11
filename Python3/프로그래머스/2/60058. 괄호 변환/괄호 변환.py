def is_correct(s: str) -> bool :
    bal = 0
    for ch in s :
        bal += 1 if ch == '(' else -1
        if bal < 0 :
            return False
    return bal == 0

def split_uv(w: str) :
    bal = 0
    for i, ch in enumerate(w) :
        bal += 1 if ch == '(' else -1
        if bal == 0 :
            return w[:i + 1], w[i + 1:]
    return w, ""  # 문제 조건상 여기 도달하지 않음

def flip(s: str) -> str :
    return ''.join('(' if ch == ')' else ')' for ch in s)

def solution(p: str) -> str :
    if not p :
        return ""
    if is_correct(p) :
        return p

    u, v = split_uv(p)
    if is_correct(u) :
        return u + solution(v)
    # 규칙 4
    return "(" + solution(v) + ")" + flip(u[1 : -1])
