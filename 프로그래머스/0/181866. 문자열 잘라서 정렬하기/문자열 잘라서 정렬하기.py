def solution(myString):
    myString = myString.replace("x"," ")
    answer = sorted(myString.split())
    return answer