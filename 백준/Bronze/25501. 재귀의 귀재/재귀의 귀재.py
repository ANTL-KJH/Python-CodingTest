"""
* Project Name : Baekjoon Online Judge #25501(재귀의 귀재)
* Program Purpose and Basic Features :
* - 재귀함수를 이용하여 피보나치 수를 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.25
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.25	    v1.0	    First Write
"""
import sys


def recursion(s, l, r):
    if l >= r:
        return 1, 1
    elif s[l] != s[r]:
        return 0, 1
    else:
        res = recursion(s, l + 1, r - 1)
        return res[0], res[1] + 1


def isPalindrome(s):
    res = recursion(s, 0, len(s) - 1)
    return res[0], res[1]


def main():
    T = int(sys.stdin.readline().rstrip())
    for _ in range(T):
        s = sys.stdin.readline().rstrip()
        palindrome = isPalindrome(s)
        print(palindrome[0], palindrome[1])


if __name__ == "__main__":
    main()
