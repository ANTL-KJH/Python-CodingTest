def solution(my_string, index_list):
    strL=[]
    for i in index_list:
        strL.append(my_string[i])
    answer = "".join(strL)
    return answer