"""
* Project Name : Baekjoon Online Judge #4948(베르트랑 공준)
* Program Purpose and Basic Features :
* - 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.17
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.17	    v1.0	    First Write
"""
import math


def main():
    while True:
        start = int(input())
        if start == 0:
            break
        end = start * 2
        Eratos = [True for _ in range(end + 1)]
        Eratos[0], Eratos[1] = False, False
        for i in range(2, int(math.sqrt(end)) + 1):
            if Eratos[i] == True:
                for j in range(2, end // i + 1):
                    Eratos[i * j] = False
        cnt = 0
        for i in range(start + 1, end + 1):
            if Eratos[i]:
                if i != 1:
                    cnt += 1
        print(cnt)


if __name__ == "__main__":
    main()
