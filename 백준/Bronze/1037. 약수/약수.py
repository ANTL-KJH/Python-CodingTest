"""
* Project Name : Baekjoon Online Judge #1037(약수)
* Program Purpose and Basic Features :
* - N 약수들이 주어졌을 때, N을 구하는 프로그램
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
    C = int(sys.stdin.readline().rstrip())
    divisorL = list(map(int, sys.stdin.readline().rstrip().split()))
    divisorL.sort()
    print(divisorL[0] * divisorL[-1])


if __name__ == "__main__":
    main()
