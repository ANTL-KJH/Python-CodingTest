"""
* Project Name : Baekjoon Online Judge #1316(그룹 단어 체커)
* Program Purpose and Basic Features :
* - 단어를 N개 입력받고 그룹 단어의 개수를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    N = int(input())
    result = 0
    for _ in range(N):
        s = input()
        duplicatedL = []
        if len(s) == 1:
            result += 1
        for i in range(1, len(s)):
            if s[i] in duplicatedL:
                break
            if s[i - 1] != s[i]:
                duplicatedL.append(s[i - 1])
            if i == len(s) - 1:
                result += 1
    print(result)


if __name__ == "__main__":
    main()
