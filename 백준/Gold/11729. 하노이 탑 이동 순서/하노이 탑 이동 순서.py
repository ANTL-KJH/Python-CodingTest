"""
* Project Name : Baekjoon Online Judge #11729(하노이 탑 이동 순서)
* Program Purpose and Basic Features :
* - 하노이탑의 이동과정을 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.25
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.25	    v1.0	    First Write
"""
import sys


def hanoi(N, start, end, bypass):
    if N == 1:
        print(start, end)
    else:
        hanoi(N - 1, start, bypass, end)
        print(start, end)
        hanoi(N - 1, bypass, end, start)


def main():
    N = int(sys.stdin.readline().rstrip())
    print(int(pow(2, N)) - 1)
    hanoi(N, 1, 3, 2)


if __name__ == "__main__":
    main()
