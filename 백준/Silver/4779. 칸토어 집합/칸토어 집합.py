"""
* Project Name : Baekjoon Online Judge #4779(칸토어 집합)
* Program Purpose and Basic Features :
* - 3의 N승 길이의 문자열을 칸토어 집합으로 만드는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.25
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.25	    v1.0	    First Write
"""
import sys


def cantor(N):
    size = int(pow(3, N - 1))
    if N == 0:
        print("-", end="")
        return
    cantor(N - 1)
    for _ in range(size):
        print(" ", end="")
    cantor(N - 1)


def main():
    while True:
        try:
            N = int(sys.stdin.readline().rstrip())
            cantor(N)
            print()
        except:
            break


if __name__ == "__main__":
    main()
