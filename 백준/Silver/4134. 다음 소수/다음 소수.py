"""
* Project Name : Baekjoon Online Judge #4134(다음 소수)
* Program Purpose and Basic Features :
* - n보다 크거나 같은 소수 중 가장 작은 소수 찾는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.16
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.16	    v1.0	    First Write
"""
import math
def isPrime(tmp):
    if tmp < 2:
        return False
    if tmp == 2 or tmp == 3:
        return True
    for i in range(2, int(math.sqrt(tmp)) + 1):
        if tmp % i == 0:
            return False
    return True

def main():
    T = int(input())
    for _ in range(T):
        inputN = int(input())
        tmp = inputN
        flag = True
        while True:
            if isPrime(tmp) == True:
                print(tmp)
                break
            else:
                tmp+=1


if __name__ == "__main__":
    main()
