"""
* Project Name : Baekjoon Online Judge #20920(영단어 암기는 괴로워)
* Program Purpose and Basic Features :
* - 주어진 길이보다 긴 단어만 정리하여 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.24
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.24	    v1.0	    First Write
"""
import sys


def main():
    wordLenD = {}
    N, M = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        ls = len(s)
        if ls >= M:
            if s in wordLenD:
                wordLenD[s] += 1
            else:
                wordLenD[s] = 1
    wordL = sorted(wordLenD.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for w in wordL:
        print(w[0])


if __name__ == "__main__":
    main()
