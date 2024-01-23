"""
* Project Name : Baekjoon Online Judge #11050(이항 계수 1)
* Program Purpose and Basic Features :
* - 자연수 N과 정수 K가 주어졌을 때 이항계수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.23
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.23	    v1.0	    First Write
"""
import sys


def main():
    N, K = map(int, sys.stdin.readline().split())
    res = 1
    divisor = 1
    if N == K or K == 0:
        print(1)
        return
    for i in range(K):
        res *= (N - i)
        divisor *= (K - i)
    print(int(res//divisor))


if __name__ == "__main__":
    main()
