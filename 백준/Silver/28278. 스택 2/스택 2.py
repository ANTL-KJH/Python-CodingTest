"""
* Project Name : Baekjoon Online Judge #28278(스택 2)
* Program Purpose and Basic Features :
* - 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.18
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.18	    v1.0	    First Write
"""
import sys

def main():
    N = int(input())
    stack = []
    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        if s[0] == '1':
            idx, num = map(int, s.split())
            stack.append(num)
        elif s[0] == '2':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack.pop())
        elif s[0] == '3':
            print(len(stack))
        elif s[0] == '4':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif s[0] == '5':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack)-1])


if __name__ == "__main__":
    main()
