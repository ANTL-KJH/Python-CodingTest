"""
* Project Name : Baekjoon Online Judge #15439(녹색거탑)
* Program Purpose and Basic Features :
* - 주어진 높이의 녹색탑에서 내려올 수 있는 경로의 경우의 수를 출력하는 프로그램
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
    print(int(pow(2,N)))


if __name__ == "__main__":
    main()
