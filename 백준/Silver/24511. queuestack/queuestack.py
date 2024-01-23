"""
* Project Name : Baekjoon Online Judge #24511(queuestack)
* Program Purpose and Basic Features :
* - queuestack에 넣을 원소들이 주어졌을 때, 해당 원소를 넣은 리턴값을 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.22
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.22	    v1.0	    First Write
* JHKIM         2024.01.23      v1.1        스택/큐 구조 변경
"""
import sys
from collections import deque


def main():
    dq = deque()
    N = int(sys.stdin.readline())
    sqL = list(map(int, sys.stdin.readline().split()))
    sqDataL = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    inputDataL = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        if sqL[i] == 0:
            dq.appendleft(sqDataL[i])
    for num in inputDataL:
        dq.append(num)
    for j in range(M):
        print(dq.popleft(), end=" ")


if __name__ == "__main__":
    main()
