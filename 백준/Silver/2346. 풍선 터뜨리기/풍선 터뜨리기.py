"""
* Project Name : Baekjoon Online Judge #2346(풍선 터뜨리기)
* Program Purpose and Basic Features :
* - 풍선에 들어있는 숫자대로 움직이며 풍선을 터뜨리는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.22
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.22	    v1.0	    First Write
"""
import sys
from collections import deque


def main():
    N = int(input())
    q = deque(enumerate(map(int, sys.stdin.readline().split())))
    ans = []

    while q:
        idx, paper = q.popleft()
        ans.append(idx + 1)

        if paper > 0:
            q.rotate(-(paper - 1))
        elif paper < 0:
            q.rotate(-paper)

    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    main()
