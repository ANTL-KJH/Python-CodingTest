"""
* Project Name : Baekjoon Online Judge #10814(나이순 정렬)
* Program Purpose and Basic Features :
* - 영어단어를 오름차순으로 정렬하는 프로그램
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
    memberL = []
    for i in range(N):
        age, name = input().split()

        memberL.append((int(age), name))

    memberL.sort(key=lambda x: x[0])
    for i in range(N):
        print(memberL[i][0], memberL[i][1])


if __name__ == "__main__":
    main()
