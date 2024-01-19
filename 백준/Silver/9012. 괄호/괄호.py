"""
* Project Name : Baekjoon Online Judge #9012(괄호)
* Program Purpose and Basic Features :
* - 주어진 괄호 문자열이 올바른 괄호 문자열(VPS)인지 판단하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.19
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.19	    v1.0	    First Write
"""
import sys


def bracket(s):
    left, right = 0, 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "(":
            left += 1
        elif s[i] == ")":
            right += 1
        if right - left < 0:
            return False
    if right-left==0:
        return True
    else:
        return False


def main():
    T = int(input())
    for _ in range(T):
        s = sys.stdin.readline().rstrip()
        if bracket(s):
            print("YES")
        else:
            print("NO")



if __name__ == "__main__":
    main()
