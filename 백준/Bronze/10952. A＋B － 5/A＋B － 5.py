"""
* Project Name : Baekjoon Online Judge #10952(A+B - 5)
* Program Purpose and Basic Features :
* - 0 0이 입력될 때 까지 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    while True:
        A, B = map(int, input().split())
        if A==0 and B==0:
            break
        print(A+B)

if __name__ == "__main__":
    main()
