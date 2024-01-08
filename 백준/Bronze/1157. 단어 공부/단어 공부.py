"""
* Project Name : Baekjoon Online Judge #1157(단어 공부)
* Program Purpose and Basic Features :
* - 가장 많이 사용된 알파벳을 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    s = input().upper()
    unique_s = list(set(s))
    cntL=[]
    for i in unique_s:
        cnt = s.count(i)
        cntL.append(cnt)
    if cntL.count(max(cntL))>1:
        print("?")
    else:
        max_index = cntL.index(max(cntL))
        print(unique_s[max_index])




if __name__ == "__main__":
    main()
