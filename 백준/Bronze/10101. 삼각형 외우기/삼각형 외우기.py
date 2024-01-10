"""
* Project Name : Baekjoon Online Judge #10101(삼각형 외우기)
* Program Purpose and Basic Features :
* - 삼각형의 세 각을 입력받은 다음 어떤 삼각형인지 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.10
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.10	    v1.0	    First Write
"""


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    if a+b+c != 180:
        print("Error")
        return
    if a ==b and a == c:
        print("Equilateral")
    elif a!=b and b!=c and c!=a:
        print("Scalene")
    else:
        print("Isosceles")

if __name__ == "__main__":
    main()
