"""
* Project Name : Baekjoon Online Judge #10798(세로읽기)
* Program Purpose and Basic Features :
* - 여러줄로 주어진 문자열을 세로로 읽는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    wordMtrx = [input() for _ in range(5)]
    for i in range(15):
        for j in range(5):
            if i <= len(wordMtrx[j]) - 1:
                print(wordMtrx[j][i], end="")


if __name__ == "__main__":
    main()
