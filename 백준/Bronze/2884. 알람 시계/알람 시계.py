"""
* Project Name : Baekjoon Online Judge #2884(알람 시계)
* Program Purpose and Basic Features :
* - 주어진 시간에서 45분 빠른 시간을 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""


def main():
    h, m = map(int, input().split())
    m = m - 45
    if m < 0:
        m = m + 60
        h = h - 1
        if h < 0:
            h = h + 24
    print(h, m)


if __name__ == "__main__":
    main()
