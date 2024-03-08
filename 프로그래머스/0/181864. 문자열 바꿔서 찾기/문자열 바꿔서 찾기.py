def solution(myString, pat):
    tmp = "".join(["B" if char == "A" else "A" for char in myString])
    
    if pat in tmp:
        answer = 1
    else:
        answer = 0
    return answer