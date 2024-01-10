"""
* Project Name : Baekjoon Online Judge #1085(직사각형에서 탈출)
* Program Purpose and Basic Features :
* - 직사각형의 가로와 세로가 주어졌을 때, 넓이를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.10
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.10	    v1.0	    First Write
"""


def main():
    x, y, w, h = map(int, input().split())
    escapeL = [x, y, w-x, h-y]
    print(min(escapeL))



if __name__ == "__main__":
    main()
