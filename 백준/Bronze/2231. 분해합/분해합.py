"""
* Project Name : Baekjoon Online Judge #2231(분해합)
* Program Purpose and Basic Features :
* - 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램
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
    result = 0
    for i in range(N):
        tmp = i
        s=tmp
        while tmp != 0:
            s += tmp%10
            tmp= tmp//10
        if s == N:
            result = i
            break
    print(result)

if __name__ == "__main__":
    main()
