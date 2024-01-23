"""
* Project Name : Baekjoon Online Judge #10872(팩토리얼)
* Program Purpose and Basic Features :
* - N 팩토리얼을 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.23
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.23	    v1.0	    First Write
"""
import sys


def main():
    N = int(sys.stdin.readline())
    res = 1
    if N == 0 or N == 1:
        print(1)
        return
    while N != 1:
        res *= N
        N -= 1
    print(res)


if __name__ == "__main__":
    main()
