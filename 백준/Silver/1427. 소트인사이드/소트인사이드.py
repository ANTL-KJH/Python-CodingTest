"""
* Project Name : Baekjoon Online Judge #1427(소트인사이드)
* Program Purpose and Basic Features :
* - 정수의 각 자리수를 내림차순으로 정렬하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    N = int(input())
    numL = []
    while N != 0:
        numL.append(N % 10)
        N //= 10
    numL.sort(reverse=True)
    for i in range(len(numL)):
        print(numL[i], end="")


if __name__ == "__main__":
    main()
