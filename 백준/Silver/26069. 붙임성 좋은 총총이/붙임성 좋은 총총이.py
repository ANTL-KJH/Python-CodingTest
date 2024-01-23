"""
* Project Name : Baekjoon Online Judge #26069(붙임성 좋은 총총이)
* Program Purpose and Basic Features :
* - 마지막에 무지개 댄스를 추는 토끼의 수를 구하는 프로그램
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
    N = int(sys.stdin.readline().rstrip())
    mettingS = set()
    mettingS.add('ChongChong')
    for _ in range(N):
        A, B = map(str, sys.stdin.readline().split())
        if A in mettingS:
            mettingS.add(B)
        if B in mettingS:
            mettingS.add(A)
    print(len(mettingS))


if __name__ == "__main__":
    main()
