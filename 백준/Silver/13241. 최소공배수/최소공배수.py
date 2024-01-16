"""
* Project Name : Baekjoon Online Judge #1934(최소공배수)
* Program Purpose and Basic Features :
* - 두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.16
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.16	    v1.0	    First Write
"""
import math


def main():
    a, b = map(int, input().split())
    print(math.lcm(a, b))


if __name__ == "__main__":
    main()
