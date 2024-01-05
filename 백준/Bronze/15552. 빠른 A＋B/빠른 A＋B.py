"""
* Project Name : Baekjoon Online Judge #15552(빠른 A+B)
* Program Purpose and Basic Features :
* - 입력이 빠른 함수를 사용하여 A+B를 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""
import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    for _ in range(N):
        A, B = map(int, sys.stdin.readline().rstrip().split())
        print(A + B)


if __name__ == "__main__":
    main()
