def solution(bin1, bin2):
    b1S, b2S = int(bin1,2),int(bin2,2)
    bitSum = b1S+b2S
    answer = bin(bitSum)[2:]
    return answer