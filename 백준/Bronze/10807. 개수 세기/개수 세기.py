"""
* Project Name : Baekjoon Online Judge #10807(개수 세기)
* Program Purpose and Basic Features :
* - N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N=int(input())
    L=list(map(int, input().split()))
    v=int(input())
    print(L.count(v))


if __name__ == "__main__":
    main()
