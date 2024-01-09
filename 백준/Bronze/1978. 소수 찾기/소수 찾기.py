"""
* Project Name : Baekjoon Online Judge #1978(소수 찾기)
* Program Purpose and Basic Features :
* - 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""

import math


def isPrime(n):
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


def main():
    N = int(input())
    numL = list(map(int, input().split()))
    result = 0
    for i in range(N):
        if numL[i] == 1:
            continue
        if isPrime(numL[i]) == True:
            result += 1

    print(result)


if __name__ == "__main__":
    main()
