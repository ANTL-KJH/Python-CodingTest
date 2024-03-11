def solution(dot):
    x, y = dot[0], dot[1]
    if x < 0:
        if y<0:
            answer = 3
        elif y>0:
            answer = 2
    elif x>0:
        if y<0:
            answer = 4
        elif y>0:
            answer = 1

    return answer