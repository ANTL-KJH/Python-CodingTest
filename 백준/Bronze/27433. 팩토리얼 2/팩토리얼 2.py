"""
* Project Name : Baekjoon Online Judge #27433(팩토리얼 2)
* Program Purpose and Basic Features :
* - 재귀함수를 이용하여 팩토리얼을 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.24
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.24	    v1.0	    First Write
"""
import sys


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    N = int(sys.stdin.readline().rstrip())
    print(factorial(N))


if __name__ == "__main__":
    main()
