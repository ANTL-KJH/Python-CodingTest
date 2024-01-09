"""
* Project Name : Baekjoon Online Judge #2720(세탁소 사장 동혁)
* Program Purpose and Basic Features :
* - 거스름돈의 동전 개수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""


def main():
    coin = [25, 10, 5, 1]
    T = int(input())
    for _ in range(T):
        change = int(input())
        for i in range(len(coin)):
            print(change//coin[i],end=" ")
            change %= coin[i]
        print()


if __name__ == "__main__":
    main()
