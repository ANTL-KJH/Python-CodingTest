"""
* Project Name : Baekjoon Online Judge #10813(공 바꾸기)
* Program Purpose and Basic Features :
* - 바구니에 들어있는 공을 교환하고 최종 상태를 출력하는 프로그램
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
    L=[i for i in range(N+1)]
    for _ in range(M):
        i, j = map(int, input().split())
        L[i],L[j]= L[j], L[i]
    for idx in range(1, N+1,1):
        print(L[idx], end=" ")

if __name__ == "__main__":
    main()
