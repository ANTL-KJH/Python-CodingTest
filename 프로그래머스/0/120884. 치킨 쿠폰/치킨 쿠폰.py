def solution(chicken):
    coupon = chicken
    answer = 0
    while coupon >= 10:
        tmp = 0
        answer += coupon// 10
        tmp = coupon//10
        coupon = coupon% 10+tmp
        
    return answer