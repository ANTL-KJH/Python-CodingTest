"""
* Project Name : Baekjoon Online Judge #2750(수 정렬하기)
* Program Purpose and Basic Features :
* - 정수를 오름차순 정렬하는 프로그램
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
    numL=[]
    for _ in range(N):
        numL.append(int(input()))
    numL.sort()
    for i in range(N):
        print(numL[i])

if __name__ == "__main__":
    main()
