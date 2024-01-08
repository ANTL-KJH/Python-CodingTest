"""
* Project Name : Baekjoon Online Judge #10988(팰린드롬인지 확인하기)
* Program Purpose and Basic Features :
* - 주어진 단어가 팰린드롬인지 판단하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    s = input()
    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - 1 - i]:
            print(0)
            return
    print(1)


if __name__ == "__main__":
    main()
