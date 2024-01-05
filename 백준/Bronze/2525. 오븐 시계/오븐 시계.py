"""
* Project Name : Baekjoon Online Judge #2525(오븐 시계)
* Program Purpose and Basic Features :
* - 주어진 시간에 분 단위 시간을 더한 결과를 출력하는 프로그램
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
    addm = int(input())
    m = m+addm
    while True:
        if m >=60:
            m=m-60
            h = h+1
        else:
            break
    while True:
        if h>=24:
            h=h-24
        else:
            break
    print(h, m)


if __name__ == "__main__":
    main()
