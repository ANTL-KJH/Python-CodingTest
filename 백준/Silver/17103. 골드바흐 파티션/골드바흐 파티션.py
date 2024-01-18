"""
* Project Name : Baekjoon Online Judge #17103(골드바흐 파티션)
* Program Purpose and Basic Features :
* - 두 소수의 합으로 나타낼 수 있는 골드바흐 파티션의 수를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.18
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.18	    v1.0	    First Write
"""
import math

MAX = 1000000


def main():
    Eratos = [True for _ in range(MAX + 1)]
    Eratos[0], Eratos[1] = False, False
    prime = []
    for i in range(2, MAX+1):
        if Eratos[i] == True:
            prime.append(i)
            tmp=2
            while i*tmp<=1000000:
                Eratos[i * tmp] = False
                tmp+=1

    T = int(input())
    for _ in range(T):
        count = 0
        N = int(input())
        for i in prime:
            if i > N // 2:
                break
            if i and Eratos[N - i]:
                count += 1
        print(count)

if __name__ == "__main__":
    main()
