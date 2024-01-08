"""
* Project Name : Baekjoon Online Judge #3052(나머지)
* Program Purpose and Basic Features :
* - 입력받은 숫자를 42로 나누어 다른 값이 몇개인지 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    divL = [0 for _ in range(42)]
    for _ in range(10):
        divL[int(input())%42]=1
    print(divL.count(1))

if __name__ == "__main__":
    main()
