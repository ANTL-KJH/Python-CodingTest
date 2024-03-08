def solution(myString):
    answer = [x if x > 'l' else 'l' for x in myString]
    answer = "".join(answer)
    return answer