"""
* Project Name : Baekjoon Online Judge #11651(좌표 정렬하기 2)
* Program Purpose and Basic Features :
* - 주어진 좌표를 y좌표를 기준으로 오름차순으로 정렬하는 프로그램
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
    posL = []
    for _ in range(N):
        posL.append(list(map(int, input().split())))
    posL.sort(key=lambda x: (x[1], x[0]))
    for pos in posL:
        print(pos[0], pos[1])


if __name__ == "__main__":
    main()
