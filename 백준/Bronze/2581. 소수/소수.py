"""
* Project Name : Baekjoon Online Judge #2581(소수)
* Program Purpose and Basic Features :
* - M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
* JHKIM         2024.01.10      v1.01       func isPrime modified
"""
import math


def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    M = int(input())
    N = int(input())
    pNumL = []
    for i in range(M, N + 1):
        if isPrime(i) == True:
            pNumL.append(i)
    if len(pNumL) == 0:
        print(-1)
    else:
        print(sum(pNumL))
        print(min(pNumL))


if __name__ == "__main__":
    main()
