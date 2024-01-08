"""
* Project Name : Baekjoon Online Judge #2908(상수)
* Program Purpose and Basic Features :
* - 주어진 두 수를 역순으로 뒤집고 그 중 큰수를 찾는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    A,B = input().split()
    A= list(A)
    A.reverse()
    A = "".join(A)

    B = list(B)
    B.reverse()
    B = "".join(B)
    print(max(A,B))

if __name__ == "__main__":
    main()
