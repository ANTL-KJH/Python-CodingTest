"""
* Project Name : Baekjoon Online Judge #18258(큐 2)
* Program Purpose and Basic Features :
* - 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
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
    q = deque([])
    for i in range(N):
        s = sys.stdin.readline().split()
        if 'push' == s[0]:
            q.append(s[1])
        elif 'pop' == s[0]:
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())
        elif 'size' == s[0]:
            print(len(q))
        elif 'empty' == s[0]:
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif 'front' == s[0]:
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])
        elif 'back' == s[0]:
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])

if __name__ == "__main__":
    main()
