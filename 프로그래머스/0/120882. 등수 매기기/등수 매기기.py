def solution(score):
    avgL = [(score[i][0]+score[i][1])/2 for i in range(len(score))]
    avgL.sort(reverse=True)
    answer = [avgL.index((score[i][0]+score[i][1])/2)+1 for i in range(len(score))]
    return answer