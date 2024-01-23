"""
* Project Name : Baekjoon Online Judge #1010(다리 놓기)
* Program Purpose and Basic Features :
* - 정수 N과 M이 주어졌을 때, 다리가 겹치지 않도록 지을 수 있는 경우의 수를 구하는 프로그램
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
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().rstrip().split())
        if N == M or N == 0:
            print(1)
            continue
        res = 1
        divisor = 1
        for i in range(N):
            res *= (M - i)
            divisor *= (N - i)
        print(res // divisor)


if __name__ == "__main__":
    main()
