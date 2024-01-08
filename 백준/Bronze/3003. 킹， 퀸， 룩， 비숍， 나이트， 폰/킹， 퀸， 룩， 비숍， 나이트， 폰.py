"""
* Project Name : Baekjoon Online Judge #3003(킹, 퀸, 룩, 비숍, 나이트, 폰)
* Program Purpose and Basic Features :
* - 보유하고 있는 피스를 통해 더하거나 뻬야하는 피스를 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    KING = 1
    QUEEN = 1
    ROOK = 2
    BISHOP = 2
    KNIGHT = 2
    PAWN = 8
    king, queen, rook, bishop, knight, pawn = map(int, input().split())
    print(KING-king,QUEEN-queen,ROOK-rook,BISHOP-bishop,KNIGHT-knight, PAWN-pawn)

if __name__ == "__main__":
    main()
