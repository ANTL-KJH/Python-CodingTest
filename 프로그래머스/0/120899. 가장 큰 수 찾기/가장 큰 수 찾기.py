def solution(array):
    ma= max(array)
    maxIdx= array.index(ma)
    answer = [ma,maxIdx]
    return answer