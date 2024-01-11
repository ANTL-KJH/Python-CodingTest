"""
* Project Name : Baekjoon Online Judge #19532(수학은 비대면강의입니다)
* Program Purpose and Basic Features :
* - 연립방정식이 주어졌을 때, 해를 찾는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    a,b,c,d,e,f = map(int,input().split())
    for x in range(-999,1000):
        for y in range(-999,1000):
            if a*x+b*y == c:
                if d*x +e*y == f:
                    print(x, y)
                    return

if __name__ == "__main__":
    main()
