"""
* Project Name : Baekjoon Online Judge #13909(창문 닫기)
* Program Purpose and Basic Features :
* - n번째 사람이 n의 배수 번째 창문을 열고 닫을 때, 열려있는 창문의 개수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.18
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.18	    v1.0	    First Write
"""


def main():
    N = int(input())
    result = 0
    x = 1
    while x * x <= N:
        x += 1
        result += 1
    print(result)


if __name__ == "__main__":
    main()
