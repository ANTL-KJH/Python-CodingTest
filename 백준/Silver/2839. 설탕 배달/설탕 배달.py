"""
* Project Name : Baekjoon Online Judge #2839(설탕 배달)
* Program Purpose and Basic Features :
* - 설탕의 무게가 주어졌을 때, 설탕봉지의 최소 개수를 출력하는 프로그램
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
    for i in range((N // 5), -1, -1):
        for j in range((N // 3), -1, -1):
            if 5 * i + 3 * j == N:
                print(i + j)
                return
    print(-1)

if __name__ == "__main__":
    main()
