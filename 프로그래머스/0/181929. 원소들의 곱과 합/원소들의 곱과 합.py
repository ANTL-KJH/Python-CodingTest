def solution(num_list):
    
    res = 1
    for i in num_list:
        res *= i
    s = sum(num_list)
    if res < s*s:
        answer = 1
    else:
        answer =0
    
    return answer