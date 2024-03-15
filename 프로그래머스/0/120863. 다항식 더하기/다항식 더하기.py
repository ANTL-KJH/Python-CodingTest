def solution(polynomial):
    polyL = list(polynomial.split())
    digit = 0
    cof = 0
    for poly in polyL:
        if poly.isdigit():
            digit += int(poly)
        else:
            if poly == "+":
                continue
            else:
                if poly =="x":
                    cof += 1
                else:
                    cof += int(poly[:-1])
    if cof >1 and digit !=0:
        answer = "{}x + {}".format(cof,digit)
    elif cof ==0 and digit != 0:
        answer = "{}".format(digit)
    elif cof > 1 and digit == 0:
        answer = "{}x".format(cof)
    elif cof == 1:
        if digit ==0:
            answer = "x"
        else:
            answer = "x + {}".format(digit)
    return answer