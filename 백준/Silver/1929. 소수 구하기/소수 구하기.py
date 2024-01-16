"""
* Project Name : Baekjoon Online Judge #1929(소수 구하기)
* Program Purpose and Basic Features :
* - M이상 N이하의 소수를 모두 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.16
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.16	    v1.0	    First Write
"""
import math


def main():
    start, end = map(int, input().split())
    Eratos = [True for _ in range(end + 1)]
    Eratos[0], Eratos[1] = False, False
    for i in range(2, int(math.sqrt(end)) + 1):
        if Eratos[i] == True:
            for j in range(2, end // i + 1):
                Eratos[i * j] = False
    for i in range(start, end + 1):
        if Eratos[i]:
            if i != 1:
                print(i)


if __name__ == "__main__":
    main()
