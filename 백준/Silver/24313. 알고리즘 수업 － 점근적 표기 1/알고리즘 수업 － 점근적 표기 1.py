"""
* Project Name : Baekjoon Online Judge #24313(알고리즘 수업 - 점근적 표기 1)
* Program Purpose and Basic Features :
* - 코드의 수행 횟수와 최고차항의 차수를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    a1, a0 = map(int, input().split())
    c = int(input())
    n0 = int(input())
    print(1 if ((a1*n0 +a0)<=c*n0)and(c-a1>=0) == True else 0)

if __name__ == "__main__":
    main()
