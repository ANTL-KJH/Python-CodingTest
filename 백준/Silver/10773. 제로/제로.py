"""
* Project Name : Baekjoon Online Judge #10773(제로)
* Program Purpose and Basic Features :
* - 0이 나올 때 마다 스택의 가장 위에 있는 수를 지우는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.19
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.19	    v1.0	    First Write
"""
import sys

def main():
    K = int(input())
    stack = []
    for _ in range(K):
        num = int(sys.stdin.readline().rstrip())
        if num == 0:
            stack.pop()
        else:
            stack.append(num)
    print(sum(stack))


if __name__ == "__main__":
    main()
