"""
* Project Name : Baekjoon Online Judge #15649(N과 M (1))
* Program Purpose and Basic Features :
* - N과 M이 주어졌을 때, 1 부터 N까지 자연수 중 중복 없이 M개를 고를 수열을 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.02.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.02.05	    v1.0	    First Write
"""
import sys


def dfs(s, visited, N, M):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs(s, visited, N, M)
        s.pop()
        visited[i] = False


def main():
    visited = [False for _ in range(9)]
    s = []
    N, M = map(int, sys.stdin.readline().rstrip().split())
    dfs(s, visited, N, M)


if __name__ == "__main__":
    main()
