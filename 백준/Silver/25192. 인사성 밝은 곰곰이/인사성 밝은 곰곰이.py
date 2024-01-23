"""
* Project Name : Baekjoon Online Judge #25192(인사성 밝은 곰곰이)
* Program Purpose and Basic Features :
* - 새로운 멤버가 입장할 때 마다 사용되는 곰곰티콘의 사용횟수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.23
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.23	    v1.0	    First Write
"""
import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    memberL=[]
    res = 0
    for _ in range(N):
        member = sys.stdin.readline().rstrip()
        if member == "ENTER":
            memberS = set(memberL)
            res += len(memberS)
            memberL=[]
        else:
            memberL.append(member)
    memberS = set(memberL)
    res += len(memberS)
    print(res)

if __name__ == "__main__":
    main()
