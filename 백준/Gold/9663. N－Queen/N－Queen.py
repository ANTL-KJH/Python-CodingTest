"""
* Project Name : Baekjoon Online Judge #9663(N-Queen)
* Program Purpose and Basic Features :
* - N x N 크기의 체스판에서 퀸 N개를 서로 공격할 수 없도록 놓는 경우의 수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.02.13
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.02.13	    v1.0	    First Write
"""
import sys

N = 0
res = 0
a, b, c = [False] * 15, [False] * (2 * 15 - 1), [False] * (2 * 15 - 1)


def NQueen(i):
    global res
    if i == N:
        res += 1
        return
    for j in range(N):
        if not (a[j] or b[i + j] or c[i - j + N - 1]):
            a[j] = b[i + j] = c[i - j + N - 1] = True
            NQueen(i + 1)
            a[j] = b[i + j] = c[i - j + N - 1] = False  # Back_Tracking


def main():
    global N
    N = int(sys.stdin.readline().rstrip())
    global res
    NQueen(0)
    print(res)


if __name__ == "__main__":
    main()
