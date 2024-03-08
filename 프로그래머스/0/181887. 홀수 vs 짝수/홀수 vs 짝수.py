def solution(num_list):
    n1 = num_list[0::2]
    n2 = num_list[1::2]
    answer = max(sum(n1), sum(n2))
    return answer