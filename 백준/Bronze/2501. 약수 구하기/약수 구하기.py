"""
* Project Name : Baekjoon Online Judge #2501(약수 구하기)
* Program Purpose and Basic Features :
* - N의 K번째 약수를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""


def main():
    N, K = map(int, input().split())
    cnt = 0
    result = 0
    for i in range(1, N + 1):
        if N % i == 0:
            cnt += 1
        if cnt == K:
            result = i
            break
    print(result)

if __name__ == "__main__":
    main()
