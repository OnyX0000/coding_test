def convert_to_base(n, base) :
    """
    n을 base진법으로 변환하는 함수.
    10~15는 A~F로 변환.
    """
    digits = "0123456789ABCDEF"
    result = ""
    
    if n == 0 :
        return "0"
    
    while n > 0 :
        result = digits[n % base] + result
        n //= base
    
    return result


def solution(n, t, m, p) :
    """
    n: 진법 (2~16)
    t: 튜브가 말해야 하는 숫자의 개수 (1~1000)
    m: 게임 참가 인원 (2~100)
    p: 튜브의 순서 (1~m)
    """
    sequence = ""
    num = 0
    
    while len(sequence) < t * m :
        sequence += convert_to_base(num, n)
        num += 1
    
    return ''.join([sequence[i] for i in range(p - 1, t * m, m)])