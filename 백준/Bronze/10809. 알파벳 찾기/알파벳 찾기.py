"""
* Project Name : Baekjoon Online Judge #10809(알파벳 찾기)
* Program Purpose and Basic Features :
* - 각각의 알파벳에 대해서, 처음 등장하는 위치를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    S = input()
    L=[-1 for _ in range(ord('z')-ord('a')+1)]
    for i in range(len(L)):
        try:
            L[i] = S.index(chr(i+ord('a')))
        except:
            continue
    for i in range(len(L)):
        print(L[i], end=" ")

if __name__ == "__main__":
    main()
