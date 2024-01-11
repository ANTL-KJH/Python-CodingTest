"""
* Project Name : Baekjoon Online Judge #1436(영화감독 숌)
* Program Purpose and Basic Features :
* - n번째로 666이 들어간 숫자를 찾는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    N = int(input())
    cnt = 0
    i = 0
    while True:
        cnt6 = 0
        tmp = i
        while tmp != 0:
            if tmp % 10 == 6:
                cnt6 += 1
            else:
                cnt6 = 0
            if cnt6 == 3:
                cnt += 1
                break
            tmp //= 10

        if cnt == N:
            print(i)
            break
        i += 1


if __name__ == "__main__":
    main()
