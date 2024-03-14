def solution(sides):
    answer = 0
    for i in range(1, sum(sides)):
        tmpL = sides+[i]
        tmpL.sort()
        if tmpL[2] < tmpL[0]+tmpL[1]:
            answer += 1
        
    
    return answer