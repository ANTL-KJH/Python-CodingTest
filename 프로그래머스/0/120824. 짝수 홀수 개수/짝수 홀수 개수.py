def solution(num_list):
    answer = [0,0]
    for i in range(len(num_list)):
        if num_list[i]%2==1:
            answer[1]+=1
        else:
            answer[0]+=1
    return answer