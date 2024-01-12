"""
* Project Name : Baekjoon Online Judge #11478(서로 다른 부분 문자열의 개수)
* Program Purpose and Basic Features :
* - 주어진 문자열에서 부분 집합을 구하고 서로 다른 부분 문자열의 개수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.12
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.12	    v1.0	    First Write
"""



def main():
    s= input()
    subset=set()
    for i in range(len(s)):
        for j in range(i,len(s)):
            subset.add(s[i:j+1])
    print(len(subset))


if __name__ == "__main__":
    main()
