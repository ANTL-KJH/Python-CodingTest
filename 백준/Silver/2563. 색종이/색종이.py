"""
* Project Name : Baekjoon Online Judge #2563(색종이)
* Program Purpose and Basic Features :
* - 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    mtrx = [list(False for _ in range(100)) for _ in range(100)]
    N = int(input())
    for _ in range(N):
        col, row = map(int, input().split())
        for i in range(row, row + 10, 1):
            for j in range(col, col + 10, 1):
                mtrx[i][j] = True
    result = 0
    for i in range(100):
        result += mtrx[i].count(True)
    print(result)


if __name__ == "__main__":
    main()
