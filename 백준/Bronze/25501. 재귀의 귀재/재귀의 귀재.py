"""
* Project Name : Baekjoon Online Judge #24060(알고리즘 수업 - 병합 정렬 1)
* Program Purpose and Basic Features :
* - 팰린드롬 여부와 확인을 위한 재귀 횟수를 출력하는 프로그램
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
