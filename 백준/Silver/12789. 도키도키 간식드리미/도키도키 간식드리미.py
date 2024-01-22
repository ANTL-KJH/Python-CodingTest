"""
* Project Name : Baekjoon Online Judge #12789(도키도키 간식드리미)
* Program Purpose and Basic Features :
* - 승환이가 간식을 받을 수 있는지 확인하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.22
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.22	    v1.0	    First Write
"""
import sys


def main():
    N = int(sys.stdin.readline().rstrip())
    studentS = list(map(int, sys.stdin.readline().rstrip().split()))
    studentS.reverse()
    tmpS = []
    target = 1
    N2 = 0
    while True:
        if N != 0 and N2 == 0:
            if studentS[N - 1] == target:
                studentS.pop()
                N -= 1
                target += 1
            else:
                tmpS.append(studentS.pop())
                N -= 1
                N2 += 1
        elif N != 0 and N2 != 0:
            if tmpS[N2 - 1] == target:
                tmpS.pop()
                N2 -= 1
                target += 1
            else:
                if studentS[N - 1] == target:
                    studentS.pop()
                    N -= 1
                    target += 1
                else:
                    tmpS.append(studentS.pop())
                    N -= 1
                    N2 += 1
        else:
            if N2 == 0:
                print("Nice")
                break
            if tmpS[N2 - 1] != target:
                print("Sad")
                break
            else:
                tmpS.pop()
                N2 -= 1
                target += 1


if __name__ == "__main__":
    main()
