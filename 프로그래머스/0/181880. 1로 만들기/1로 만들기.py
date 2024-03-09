def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        while num_list[i]!=1:
            num_list[i]=int(num_list[i]/2)
            answer +=1
    return answer