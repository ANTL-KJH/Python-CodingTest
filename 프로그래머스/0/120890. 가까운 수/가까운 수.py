def solution(array, n):
    diff_min=101
    answer = 0
    array.sort()
    for i in range(len(array)):
        new_diff = abs(array[i]-n)
        if new_diff < diff_min:
            diff_min = new_diff
            answer = array[i]
            
    return answer