"""
* Project Name : Baekjoon Online Judge #10815(숫자 카드)
* Program Purpose and Basic Features :
* - 주어진 카드를 가지고 있는지 판단하는 프로그램
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
    targetCardL = list(map(int, input().split()))
    targetCardD = {}
    for i in range(N):
        targetCardD[targetCardL[i]] = True
    M = int(input())
    givenCardL = list(map(int, input().split()))
    for i in range(M):
        if givenCardL[i] in targetCardD:
            print(1, end=" ")
        else:
            print(0, end=" ")


if __name__ == "__main__":
    main()
