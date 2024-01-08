"""
* Project Name : Baekjoon Online Judge #10810(공 넣기)
* Program Purpose and Basic Features :
* - 주어진 조건에 따라 공을 넣었을 때, 마지막에 바구니에 들어있는 공을 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N,M=map(int,input().split())
    L=[0 for _ in range(N+1)]
    for i in range(M):
        start, end, ball = map(int, input().split())
        for idx in range(start,end+1,1):
            L[idx] = ball
    for idx in range(1, N+1,1):
        print(L[idx], end=" ")

if __name__ == "__main__":
    main()
