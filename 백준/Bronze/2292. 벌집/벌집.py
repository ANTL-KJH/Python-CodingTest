"""
* Project Name : Baekjoon Online Judge #2292(벌집)
* Program Purpose and Basic Features :
* - 1번방에서 N번방으로 가는데 몇개의 방을 통과해야하는지 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""


def main():
    N = int(input())
    N -= 1
    d = 1
    if N == 0:
        print(1)
        return
    while True:
        N -= 6 * d
        if N <= 0:
            print(d + 1)
            break
        d += 1


if __name__ == "__main__":
    main()
