def solution(chicken):
    serv = 0
    coupons = chicken

    while coupons >= 10 :
        new = coupons // 10
        serv += new
        coupons = new + (coupons % 10)

    return serv