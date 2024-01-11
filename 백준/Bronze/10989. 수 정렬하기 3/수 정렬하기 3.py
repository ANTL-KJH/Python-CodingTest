"""
* Project Name : Baekjoon Online Judge #10989(수 정렬하기 3)
* Program Purpose and Basic Features :
* - 정수를 오름차순 정렬하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""
import sys


def main():
    N = int(input())
    arr = [0] * (10000 + 1)
    for _ in range(N):
        arr[int(sys.stdin.readline())] += 1
    for i in range(len(arr)):
        if arr[i] != 0:
            for _ in range(arr[i]):
                print(i)


if __name__ == "__main__":
    main()
