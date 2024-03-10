import re
def solution(myStr):
    answer = myStr.replace("a"," ")
    answer = answer.replace("b"," ")
    answer = answer.replace("c"," ")
    answer = answer.split()
    if answer == []:
        answer = ["EMPTY"]
    return answer