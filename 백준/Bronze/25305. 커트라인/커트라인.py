"""
* Project Name : Baekjoon Online Judge #25305(커트라인)
* Program Purpose and Basic Features :
* - 정수를 내림차순 정렬하여 수상 커트라인을 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    N, k = map(int, input().split())
    numL = list(map(int, input().split()))
    numL.sort(reverse=True)
    print(numL[k - 1])


if __name__ == "__main__":
    main()
