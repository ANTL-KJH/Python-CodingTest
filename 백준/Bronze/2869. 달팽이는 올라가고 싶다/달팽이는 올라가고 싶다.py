"""
* Project Name : Baekjoon Online Judge #2869(달팽이는 올라가고 싶다)
* Program Purpose and Basic Features :
* - 달팽이가 나무에 오를 때, 얼마만에 올라갈 수 있는지 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""
import math

def main():
    A, B, V = map(int, input().split())
    k = (V-B)/(A-B)
    print(math.ceil(k))



if __name__ == "__main__":
    main()
