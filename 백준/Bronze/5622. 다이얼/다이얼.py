"""
* Project Name : Baekjoon Online Judge #5622(다이얼)
* Program Purpose and Basic Features :
* - 다이얼의 문자를 숫자로 변환하고 시간을 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    dial = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    S = input()
    result=0
    for i in range(len(S)):
        for d in range(2, len(dial)):
            try:
                dial[d].index(S[i])
                result += d+1
            except:
                continue
    print(result)
if __name__ == "__main__":
    main()
