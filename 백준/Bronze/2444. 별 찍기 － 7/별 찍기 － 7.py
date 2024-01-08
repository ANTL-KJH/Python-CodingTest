"""
* Project Name : Baekjoon Online Judge #2444(별 찍기 - 7)
* Program Purpose and Basic Features :
* - 입력된 수에 맞게 별을 출력하는 프로그램
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
    for i in range(1, N + 1):
        print(' ' * (N - i) + '*' * (2 * i - 1))
    for i in range(N - 1, 0, -1):
        print(' ' * (N - i) + '*' * (2 * i - 1))

if __name__ == "__main__":
    main()
