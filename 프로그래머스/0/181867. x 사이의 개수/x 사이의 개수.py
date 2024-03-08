def solution(myString):
    myString = list(myString.split(sep="x"))
    answer = [len(st) for st in myString]
    return answer