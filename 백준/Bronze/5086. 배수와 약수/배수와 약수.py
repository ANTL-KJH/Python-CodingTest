"""
* Project Name : Baekjoon Online Judge #5086(배수와 약수)
* Program Purpose and Basic Features :
* - 두 수가 배수, 약수의 관계인지 파악하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""


def main():
    while True:
        A, B = map(int, input().split())
        if A == 0 and B == 0:
            break
        if A % B == 0:
            print("multiple")
        elif B % A == 0:
            print("factor")
        else:
            print("neither")


if __name__ == "__main__":
    main()
