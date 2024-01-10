"""
* Project Name : Baekjoon Online Judge #5073(삼각형과 세 변)
* Program Purpose and Basic Features :
* - 주어진 세 변의 길이를 통해 어떤 삼각형인지 구분하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.10
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.10	    v1.0	    First Write
"""


def main():
    while True:
        a, b, c = map(int, input().split())
        if a == 0 and b == 0 and c == 0:
            break
        if a + b <= c or b + c <= a or c + a <= b:
            print("Invalid")
            continue
        if a == b and b == c:
            print("Equilateral")
        elif a!= b and b!=c and c!=a:
            print("Scalene")
        else:
            print("Isosceles")


if __name__ == "__main__":
    main()
