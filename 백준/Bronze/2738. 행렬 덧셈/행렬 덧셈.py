"""
* Project Name : Baekjoon Online Judge #2738(행렬 덧셈)
* Program Purpose and Basic Features :
* - N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N,M=map(int,input().split())
    mA, mB = [],[]
    for i in range(N):
        mA.append(list(map(int, input().split())))
    for i in range(N):
        mB.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(M):
            print(mA[i][j]+mB[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
