"""
* Project Name : Baekjoon Online Judge #2588
* Program Purpose and Basic Features :
* - BOJ-Python #2588
* Program Author : JHKIM
* Date of original creation : 2024.01.02
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.02	    v1.0	    First Write
"""


def main():
    A = int(input())
    B = int(input())
    print(A * (B % 10))
    print(A * ((B % 100) // 10))
    print(A * (B // 100))
    print(A * B)


if __name__ == "__main__":
    main()
