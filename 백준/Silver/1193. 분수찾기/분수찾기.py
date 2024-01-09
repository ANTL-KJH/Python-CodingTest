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
    X = int(input())
    N = 1
    while True:
        total = N * (2 + N - 1) / 2
        N += 1
        if X <= total:
            remainder = -int(X - (N - 1) * (2 + N - 2) / 2)
            break

    numerator = 1
    dominator = N - 1
    for i in range(remainder):
        numerator += 1
        dominator -= 1
    if N % 2 == 1:
        numerator, dominator = dominator, numerator
    print("{}/{}".format(numerator, dominator))


if __name__ == "__main__":
    main()
