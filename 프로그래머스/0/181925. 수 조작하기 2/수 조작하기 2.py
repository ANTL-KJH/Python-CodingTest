def solution(numLog):
    answer = ""
    for i in range(1, len(numLog)):
        if numLog[i]-1 == numLog[i-1]:
            answer +="w"
        elif numLog[i]-10 == numLog[i-1]:
            answer += "d"
        elif numLog[i]+1 == numLog[i-1]:
            answer +="s"
        elif numLog[i]+10 == numLog[i-1]:
            answer +="a"
            
    return answer