"""
* Project Name : Baekjoon Online Judge #2562(최댓값)
* Program Purpose and Basic Features :
* - 9개의 서로 다른 자연수가 주어질 때, 최댓값을 찾고 몇 번째 수인지를 구하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    L = []
    maxN = 0
    maxIdx = 0
    for i in range(9):
        L.append(int(input()))
        if L[i] > maxN:
            maxN = L[i]
            maxIdx = i
    print(maxN)
    print(maxIdx+1)


if __name__ == "__main__":
    main()
