"""
* Project Name : Baekjoon Online Judge #2108(통계학)
* Program Purpose and Basic Features :
* - 입력된 수들의 산술평균, 중앙값, 최빈값, 범위를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.23
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.23	    v1.0	    First Write
"""
import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    numCountL = [0 for _ in range(8001)]
    numL = []
    maxCount = 0
    maxCountL = []
    for _ in range(N):
        num = int(sys.stdin.readline().rstrip())
        numL.append(num)
        numCountL[num] += 1
    numL.sort()
    numS = set(numL)
    for n in numS:
        if numCountL[n] > maxCount:
            maxCount = numCountL[n]
    for n in numS:
        if numCountL[n] == maxCount:
            maxCountL.append(n)
    maxCountL.sort()
    print(round(sum(numL) / len(numL)))
    print(numL[len(numL) // 2])
    print(maxCountL[0] if len(maxCountL) == 1 else maxCountL[1])
    print(numL[-1] - numL[0])


if __name__ == "__main__":
    main()
