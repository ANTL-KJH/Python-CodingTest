"""
* Project Name : Baekjoon Online Judge #11005(진법 변환2)
* Program Purpose and Basic Features :
* - 10진법 숫자를 B진법으로 바꿔 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""


def main():
    N, B = map(int, input().split())
    s=""
    arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while N:
        s += str(arr[N % B])
        N = N//B
    print(s[::-1])


if __name__ == "__main__":
    main()
