"""
* Project Name : Baekjoon Online Judge #10816(숫자 카드 2)
* Program Purpose and Basic Features :
* - 주어진 수가 적혀있는 카드를 몇개 가지고 있는지 확인하는 프로그램
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
    N = int(input())
    ndict={}
    for k in input().split():
        if int(k) in ndict:
            ndict[int(k)] += 1
        else:
            ndict[int(k)] = 1
    M=int(input())
    for fk in input().split():
        if int(fk) in ndict:
            print(ndict[int(fk)], end=" ")
        else:
            print(0, end=" ")

if __name__ == "__main__":
    main()
