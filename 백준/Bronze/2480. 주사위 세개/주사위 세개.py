"""
* Project Name : Baekjoon Online Judge #2480(주사위 세개)
* Program Purpose and Basic Features :
* - 주어진 주사위 눈에 따라 상금을 계산하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.05
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.05	    v1.0	    First Write
"""


def main():
    dice = list(map(int, input().split()))

    if dice[0] == dice[1] == dice[2]:
        print(10000 + dice[0] * 1000)
    elif dice[0] == dice[1]:
        print(1000 + dice[0] * 100)
    elif dice[0] == dice[2]:
        print(1000 + dice[0] * 100)
    elif dice[1] == dice[2]:
        print(1000 + dice[1] * 100)
    else:
        print(100 * max(dice[0], dice[1], dice[2]))


if __name__ == "__main__":
    main()
