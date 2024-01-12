"""
* Project Name : Baekjoon Online Judge #14425(문자열 집합)
* Program Purpose and Basic Features :
* - 몇 개의 문자열이 집합에 포함되는지 세는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.12
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.12	    v1.0	    First Write
"""


def main():
    N, M = map(int, input().split())
    strD = {}
    cnt = 0
    for _ in range(N):
        strD[input()]= True
    for _ in range(M):
        if input() in strD:
            cnt+=1
    print(cnt)



if __name__ == "__main__":
    main()
