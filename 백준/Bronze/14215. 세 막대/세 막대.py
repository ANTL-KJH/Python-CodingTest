"""
* Project Name : Baekjoon Online Judge #14215(세 막대)
* Program Purpose and Basic Features :
* - 주어진 세 막대로 둘레가 가장 긴 삼각형을 만드는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.10
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.10	    v1.0	    First Write
"""


def main():
    triL = []
    a, b, c = map(int, input().split())
    triL.append(a)
    triL.append(b)
    triL.append(c)
    triL.sort()
    if triL[2]>= triL[0]+triL[1]:
        triL[2] = triL[0]+triL[1]-1
    print(sum(triL))

if __name__ == "__main__":
    main()
