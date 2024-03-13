def solution(box, n):
    x, y, z = box[0]//n, box[1]//n, box[2]//n
    answer = x*y*z
    return answer