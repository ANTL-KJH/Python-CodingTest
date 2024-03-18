def solution(quiz):
    answer = []
    for qu in quiz:
        if eval(qu[:qu.find("=")]) == int(qu[qu.find("=")+1:]):
            answer.append("O")
        else:
            answer.append("X")
    
    return answer