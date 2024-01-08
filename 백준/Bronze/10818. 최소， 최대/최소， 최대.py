"""
* Project Name : Baekjoon Online Judge #10818(최소, 최대)
* Program Purpose and Basic Features :
* - N개의 정수가 주어질 때, 최솟값과 최댓값을 구하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N= int(input())
    L = list(map(int, input().split()))
    print(min(L),max(L))


if __name__ == "__main__":
    main()
