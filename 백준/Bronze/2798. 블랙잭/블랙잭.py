"""
* Project Name : Baekjoon Online Judge #2798(블랙잭)
* Program Purpose and Basic Features :
* - N장의 카드가 주어졌을 때, M을 넘지 않고 M에 최대한 가까운 카드 3장의 합을 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    N, M = map(int, input().split())
    numL = list(map(int, input().split()))
    result=0
    for a in range(N - 2):
        for b in range(a+1, N - 1):
            for c in range(b+1, N):
                snum =numL[a]+numL[b]+numL[c]
                if snum <M and snum>result:
                    result = snum
                elif snum == M:
                    result = snum
                    break
    print(result)


if __name__ == "__main__":
    main()
