"""
* Project Name : Baekjoon Online Judge #10430
* Program Purpose and Basic Features :
* - BOJ-Python #10430
* Program Author : JHKIM
* Date of original creation : 2024.01.02
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.02	    v1.0	    First Write
"""


def main():
    A, B, C = map(int,input().split())
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)



if __name__ == "__main__":
    main()
