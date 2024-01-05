"""
* Project Name : Baekjoon Online Judge #2753(윤년)
* Program Purpose and Basic Features :
* - 연도를 입력받고 윤년인지 구분하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""


def main():
    y = int(input())
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
