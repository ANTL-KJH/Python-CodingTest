"""
* Project Name : Baekjoon Online Judge #2485(가로수)
* Program Purpose and Basic Features :
* - 모든 가로수가 같은 간격이 되도록 새로 심어야 하는 가로수의 최소수를 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.16
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.16	    v1.0	    First Write
"""
import math


def main():
    pos = []
    diff = []
    N = int(input())
    pos.append(int(input()))
    for i in range(1, N):
        pos.append(int(input()))
        diff.append(pos[i] - pos[i - 1])
    diffGcd = math.gcd(*diff)
    ans = (pos[-1]-pos[0])//diffGcd+1
    print(ans-N)

if __name__ == "__main__":
    main()
