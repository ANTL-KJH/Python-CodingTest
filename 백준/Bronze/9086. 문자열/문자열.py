"""
* Project Name : Baekjoon Online Judge #9086(문자열)
* Program Purpose and Basic Features :
* - 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    T = int(input())
    for _ in range(T):
        S=input()
        print(S[0]+S[-1])

if __name__ == "__main__":
    main()
