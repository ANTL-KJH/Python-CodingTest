"""
* Project Name : Baekjoon Online Judge #1018(체스판 다시 칠하기)
* Program Purpose and Basic Features :
* - 8*8 크기의 체스판을 만들 때, 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    N, M = map(int, input().split())
    chessboard = []
    result = 64
    for i in range(N):
        chessboard.append(input())
    for i in range(N - 7):
        for j in range(M - 7):
            cnt1 = 0
            cnt2 = 0
            for x in range(8):
                for y in range(8):
                    if (x + y) % 2 == 0:
                        if chessboard[i + x][j + y] == 'W':
                            cnt1 += 1
                        else:
                            cnt2 += 1
                    else:
                        if chessboard[i + x][j + y] == 'B':
                            cnt1 += 1
                        else:
                            cnt2 += 1
            result = min(result, cnt1, cnt2)
    print(result)

if __name__ == "__main__":
    main()
