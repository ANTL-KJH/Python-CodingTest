"""
* Project Name : Baekjoon Online Judge #2739(구구단)
* Program Purpose and Basic Features :
* - 숫자를 입력받고 해당 단을 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""


def main():
    N=int(input())
    for i in range(1,10,1):
        print("{} * {} = {}".format(N,i,N*i))


if __name__ == "__main__":
    main()
