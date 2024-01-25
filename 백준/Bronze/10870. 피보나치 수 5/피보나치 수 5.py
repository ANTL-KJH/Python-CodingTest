"""
* Project Name : Baekjoon Online Judge #10870(피보나치 수 5)
* Program Purpose and Basic Features :
* - 재귀함수를 이용하여 피보나치 수를 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.24
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.24	    v1.0	    First Write
"""
import sys


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    N = int(sys.stdin.readline().rstrip())
    print(fibonacci(N))


if __name__ == "__main__":
    main()
