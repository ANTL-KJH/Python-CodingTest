"""
* Project Name : Baekjoon Online Judge #15439(베라의 패션)
* Program Purpose and Basic Features :
* - N벌의 상의와 N벌의 하의가 있을 때 가능한 조합 가짓수를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.23
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.23	    v1.0	    First Write
"""
import sys


def main():
    N = int(sys.stdin.readline())
    print(N * (N - 1))


if __name__ == "__main__":
    main()
