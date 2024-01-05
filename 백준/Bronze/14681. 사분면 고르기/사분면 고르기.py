"""
* Project Name : Baekjoon Online Judge #14681(사분면 고르기)
* Program Purpose and Basic Features :
* - x,y 좌표를 입력받고 어느 사분면에 속하는지 판단하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""


def main():
    x = int(input())
    y = int(input())
    if x>0:
        if y>0:
            print(1)
        elif y<0:
            print(4)
    elif x<0:
        if y>0:
            print(2)
        elif y<0:
            print(3)


if __name__ == "__main__":
    main()
