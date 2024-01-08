"""
* Project Name : Baekjoon Online Judge #2438(별찍기 - 1)
* Program Purpose and Basic Features :
* - 정수를 입력받고 증가하는 별을 그리는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N = int(input())
    for i in range(1, N + 1, 1):
        for _ in range(i):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()
