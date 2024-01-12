"""
* Project Name : Baekjoon Online Judge #1269(대칭 차집합)
* Program Purpose and Basic Features :
* - 대칭 차집합의 원소 개수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.12
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.12	    v1.0	    First Write
"""
import sys


def main():
    N, M = map(int, input().split())
    setA = set(input().split())
    setB = set(input().split())
    print(len(setA - setB) + len(setB - setA))


if __name__ == "__main__":
    main()
