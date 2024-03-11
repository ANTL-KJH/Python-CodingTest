def solution(my_string):
    answer = 0
    for i in my_string:
        if i<="9" and i>="0":
            answer += int(i)
    return answer