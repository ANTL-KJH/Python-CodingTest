"""
* Project Name : Baekjoon Online Judge #1764(듣보잡)
* Program Purpose and Basic Features :
* - 주어진 이름이 등록된 이름인지 확인하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.12
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.12	    v1.0	    First Write
"""
import sys

def main():
    nameD={}
    N, M = map(int, input().split())
    for _ in range(N):
        nameD[input()]=True
    cnt =0
    findL=[]
    for _ in range(M):
        findName = input()
        if findName in nameD:
            cnt +=1
            findL.append(findName)
    findL.sort()
    print(cnt)
    for name in findL:
        print(name)
if __name__ == "__main__":
    main()
