"""
* Project Name : Baekjoon Online Judge #9063(대지)
* Program Purpose and Basic Features :
* - 주어진 점을 포함하는 최소크기의 사각형 넓이를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.10
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.10	    v1.0	    First Write
"""


def main():
    xL, yL = [], []
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        xL.append(x)
        yL.append(y)
    print((max(xL)-min(xL))*(max(yL)-min(yL)))

if __name__ == "__main__":
    main()
