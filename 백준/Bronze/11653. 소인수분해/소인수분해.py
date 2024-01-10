"""
* Project Name : Baekjoon Online Judge #11653(소인수분해)
* Program Purpose and Basic Features :
* - 정수 N이 주어졌을 때, 소인수분해하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.10
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.10	    v1.0	    First Write
"""
import math


def main():
    N = int(input())
    if N == 1:
        return
    d = 2
    while True:
        if N == 1:
            break
        if N % d == 0:
            print(d)
            N /= d
        else:
            d += 1


if __name__ == "__main__":
    main()
