"""
* Project Name : Baekjoon Online Judge #27866(문자와 문자열)
* Program Purpose and Basic Features :
* - 단어S와 정수i가 주어졌을 때, i번째 문자를 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    S = input()
    i = int(input())
    print(S[i-1])


if __name__ == "__main__":
    main()
