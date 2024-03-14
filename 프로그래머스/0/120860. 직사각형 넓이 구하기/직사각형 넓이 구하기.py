def solution(dots):
    xL, yL = [pos[0] for pos in dots],[pos[1] for pos in dots]
    answer = (max(xL)-min(xL))*(max(yL)-min(yL))
    return answer