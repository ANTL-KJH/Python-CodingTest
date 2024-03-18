import math
def solution(numer1, denom1, numer2, denom2):
    gcd1 = math.gcd(numer1,denom1)
    gcd2 = math.gcd(numer2,denom2)
    numer1 //= gcd1
    denom1 //= gcd1
    numer2 //= gcd2
    denom2 //= gcd2
    lcm = (denom1*denom2)//math.gcd(denom1,denom2)
    
    answer = [numer1*(lcm//denom1)+numer2*(lcm//denom2), lcm]
    gcd = math.gcd(answer[0],answer[1])
    if gcd != 1:
        answer[0], answer[1] = answer[0]//gcd, answer[1]//gcd
    return answer