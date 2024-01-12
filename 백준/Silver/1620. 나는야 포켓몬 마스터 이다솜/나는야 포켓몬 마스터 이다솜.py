"""
* Project Name : Baekjoon Online Judge #1620(나는야 포켓몬 마스터 이다솜)
* Program Purpose and Basic Features :
* - 입력에 따라 포켓몬 이름 또는 번호를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.12
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.12	    v1.0	    First Write
"""
import sys

def main():
    N, M = map(int, input().split())
    pokemonDs = {}
    pokemonDi = {}
    for i in range(1, N+1):
        s = sys.stdin.readline().rstrip()
        pokemonDs[s] = i
        pokemonDi[i] = s
    for j in range(M):
        findS=sys.stdin.readline().rstrip()
        if findS.isdigit():
            print(pokemonDi[int(findS)])
        else:
            print(pokemonDs[findS])


if __name__ == "__main__":
    main()
