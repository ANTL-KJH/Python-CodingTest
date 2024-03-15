def solution(A, B):
    AL = list(A)
    answer = -1
    for i in range(len(AL)):
        if "".join(AL) == B:
            answer = i
            break
        AL.insert(0, AL.pop(len(AL)-1))
    
    return answer