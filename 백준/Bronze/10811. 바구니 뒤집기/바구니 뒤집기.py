"""
* Project Name : Baekjoon Online Judge #10811(바구니 뒤집기)
* Program Purpose and Basic Features :
* - 입력받은 구간의 숫자를 역순으로 배열하는 프로그램
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
    L=[i+1 for i in range(N)]
    for _ in range(M):
        i,j = map(int, input().split())
        L[i-1:j]=reversed(L[i-1:j])
    for idx in range(N):
        print(L[idx],end=" ")

if __name__ == "__main__":
    main()
