"""
* Project Name : Baekjoon Online Judge #1181(단어 정렬)
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
    wordL = []
    for _ in range(N):
        word = input()
        if word not in wordL:
            wordL.append(word)
    wordL.sort(key= lambda x: (len(x), x))
    for i in range(len(wordL)):
        print(wordL[i])


if __name__ == "__main__":
    main()
