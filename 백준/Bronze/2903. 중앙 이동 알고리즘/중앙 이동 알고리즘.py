"""
* Project Name : Baekjoon Online Judge #2903(중앙 이동 알고리즘)
* Program Purpose and Basic Features :
* - 정사각형의 각 변의 중앙에 점을 추가할 때, 총 몇개의 점을 저장해야하는지 구하는 프로그램
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
    r = 2
    for i in range(1, N + 1):
        r += pow(2, i - 1)
    print(r * r)


if __name__ == "__main__":
    main()
