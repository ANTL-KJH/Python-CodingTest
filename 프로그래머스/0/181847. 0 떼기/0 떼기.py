def solution(n_str):
    n_str = list(n_str)
    for i in range(len(n_str)):
        if n_str[i] != "0":
            answer = "".join(n_str[i:])
            break
    return answer