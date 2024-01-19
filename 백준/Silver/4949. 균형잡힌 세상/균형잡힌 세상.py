"""
* Project Name : Baekjoon Online Judge #4949(균형잡힌 세상)
* Program Purpose and Basic Features :
* - 주어진 문자열이 균형잡혀있는지 확인하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.19
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.19	    v1.0	    First Write
"""
import sys


def bracketValid(s):
    stack = []
    for ch in s:
        if ch == "[" or ch == "(":
            stack.append(ch)
            continue
        if ch == "]" or ch == ")":
            if len(stack) == 0:
                return False
            else:
                if ch == "]":
                    if stack.pop() == "[":
                        continue
                    else:
                        return False
                if ch == ")":
                    if stack.pop() == "(":
                        continue
                    else:
                        return False
    if len(stack) == 0:
        return True
    else:
        return False


def main():
    while True:
        s = sys.stdin.readline().rstrip()
        if s == ".":
            break
        if bracketValid(s) == True:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    main()
