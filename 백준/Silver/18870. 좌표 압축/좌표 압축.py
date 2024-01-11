"""
* Project Name : Baekjoon Online Judge #18870(좌표 압축)
* Program Purpose and Basic Features :
* - 주어진 좌표를 압축하는 프로그램
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
    posL =list(map(int,input().split()))
    sorted_posL = sorted(list(set(posL)))
    numDict={}
    for i in range(len(sorted_posL)):
        numDict[sorted_posL[i]]=i
    for i in range(N):
        print(numDict[posL[i]], end=" ")



if __name__ == "__main__":
    main()
