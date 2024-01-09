"""
* Project Name : Baekjoon Online Judge #2566(최댓값)
* Program Purpose and Basic Features :
* - 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    row, col = 0, 0
    mtrx = []
    maxL = []
    for i in range(9):
        mtrx.append(list(map(int, input().split())))
    for i in range(9):
        maxL.append(max(mtrx[i]))
    maxN=max(maxL)
    row = maxL.index(maxN)
    col = mtrx[row].index(maxN)
    print(maxN)
    print(row+1, col+1)

if __name__ == "__main__":
    main()
