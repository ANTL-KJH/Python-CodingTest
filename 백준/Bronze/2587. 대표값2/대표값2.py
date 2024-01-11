"""
* Project Name : Baekjoon Online Judge #2587(대표값2)
* Program Purpose and Basic Features :
* - 정수를 오름차순 정렬하고 평균과 중앙값을 찾는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.11
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.11	    v1.0	    First Write
"""


def main():
    numL = []
    for _ in range(5):
        numL.append(int(input()))
    numL.sort()
    print(sum(numL) // 5)
    print(numL[2])


if __name__ == "__main__":
    main()
