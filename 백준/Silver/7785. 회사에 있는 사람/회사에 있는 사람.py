"""
* Project Name : Baekjoon Online Judge #7785(회사에 있는 사람)
* Program Purpose and Basic Features :
* - 주어진 출입 기록으로 회사이 있는 사람을 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.12
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.12	    v1.0	    First Write
"""


def main():
    N = int(input())
    enterD = {}
    for _ in range(N):
        name, state = input().split()
        if state == "enter":
            enterD[name] = state
        else:
            del enterD[name]

    for name in sorted(enterD, reverse=True):
        print(name)


if __name__ == "__main__":
    main()
