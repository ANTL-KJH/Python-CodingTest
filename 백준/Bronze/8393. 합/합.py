"""
* Project Name : Baekjoon Online Judge #8393(합)
* Program Purpose and Basic Features :
* - n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""


def main():
    n=int(input())
    print(int(n*(2+(n-1))/2))

if __name__ == "__main__":
    main()
