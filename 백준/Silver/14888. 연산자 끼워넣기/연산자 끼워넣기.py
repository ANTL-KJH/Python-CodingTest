"""
* Project Name : Baekjoon Online Judge #14888(연산자 끼워넣기)
* Program Purpose and Basic Features :
* - 주어질 수열의 수와 수 사이에 연산자를 끼워 넣어 계산한 결과의 최대값과 최소값을 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.02.29
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.02.29	    v1.0	    First Write
"""
import sys

N = 0
numL = []
operatorL = []
res = []


def dfs(count, tmp):
    if count == N:
        res.append(tmp)
        return
    for i in range(4):
        if operatorL[i] != 0:
            operatorL[i] -= 1
            if i == 0:
                dfs(count + 1, tmp + numL[count + 1])
            elif i == 1:
                dfs(count + 1, tmp - numL[count + 1])
            elif i == 2:
                dfs(count + 1, tmp * numL[count + 1])
            elif i == 3:
                dfs(count + 1, int(tmp / numL[count + 1]))
            operatorL[i] += 1


def main():
    global N
    global numL
    global operatorL
    N = int(sys.stdin.readline().rstrip()) - 1
    numL = list(map(int, sys.stdin.readline().rstrip().split()))
    operatorL = list(map(int, sys.stdin.readline().rstrip().split()))

    dfs(0, numL[0])

    print(max(res))
    print(min(res))


if __name__ == "__main__":
    main()
