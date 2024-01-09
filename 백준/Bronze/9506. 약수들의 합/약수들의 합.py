"""
* Project Name : Baekjoon Online Judge #9506(약수들의 합)
* Program Purpose and Basic Features :
* - n이 완전수인지 아닌지 판단하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""


def main():
    while True:
        factor = []
        n = int(input())
        if n == -1:
            break
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                factor.append(i)
        if sum(factor) == n:
            print("{} = ".format(n), " + ".join(str(i) for i in factor), sep="")
        else:
            print("{} is NOT perfect.".format(n))


if __name__ == "__main__":
    main()
