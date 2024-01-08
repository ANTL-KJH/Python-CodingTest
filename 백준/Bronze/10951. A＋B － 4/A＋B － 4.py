"""
* Project Name : Baekjoon Online Judge #10951(A+B - 4)
* Program Purpose and Basic Features :
* - 입력이 끝날 때 까지 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
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
        try:
            A, B = map(int, input().split())
            print(A+B)
        except:
            break

if __name__ == "__main__":
    main()
