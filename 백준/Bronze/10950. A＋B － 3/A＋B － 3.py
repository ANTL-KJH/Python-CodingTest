"""
* Project Name : Baekjoon Online Judge #10950(A+B - 3)
* Program Purpose and Basic Features :
* - 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""


def main():
    T=int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(A+B)


if __name__ == "__main__":
    main()
