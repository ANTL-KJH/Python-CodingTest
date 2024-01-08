"""
* Project Name : Baekjoon Online Judge #1546(평균)
* Program Purpose and Basic Features :
* - 최댓값을 찾고 최댓값에 따라 달라진 수들의 평균을 구하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N = int(input())
    L = list(map(int, input().split()))
    maxL = max(L)
    for i in range(N):
        L[i] = L[i] / maxL * 100
    print(sum(L) / N)


if __name__ == "__main__":
    main()
