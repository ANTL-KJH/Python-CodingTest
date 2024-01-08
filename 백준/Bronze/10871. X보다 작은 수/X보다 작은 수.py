"""
* Project Name : Baekjoon Online Judge #10871(X보다 작은 수)
* Program Purpose and Basic Features :
* - 수열에서 X보다 작은 수를 모두 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    for i in range(N):
        if L[i] < X:
            print(L[i], end=" ")


if __name__ == "__main__":
    main()
