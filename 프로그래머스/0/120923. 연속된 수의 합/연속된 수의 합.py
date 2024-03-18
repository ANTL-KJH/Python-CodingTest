def solution(num, total):
    avg = total // num
    answer = [i for i in range(avg-(num-1)//2, avg+(num+2)//2)]
    return answer