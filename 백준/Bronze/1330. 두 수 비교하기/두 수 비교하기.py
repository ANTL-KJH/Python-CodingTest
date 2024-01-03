"""
* Project Name : Baekjoon Online Judge #1330(두 수 비교하기)
* Program Purpose and Basic Features :
* - 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.03
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.03	    v1.0	    First Write
"""


def main():
    A, B = map(int, input().split())
    if A > B:
        print(">")
    elif A == B:
        print("==")
    else:
        print("<")


if __name__ == "__main__":
    main()
