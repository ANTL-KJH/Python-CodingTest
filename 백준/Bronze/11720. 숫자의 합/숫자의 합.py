"""
* Project Name : Baekjoon Online Judge #11720(숫자의 합)
* Program Purpose and Basic Features :
* - 문자열로 주어진 수들을 덧셈하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N = int(input())
    S = input()
    result = 0
    for i in range(N):
        result = result + int(S[i])
    print(result)


if __name__ == "__main__":
    main()
