"""
* Project Name : Baekjoon Online Judge #5597(과제 안 내신 분..?)
* Program Purpose and Basic Features :
* - 1부터 30까지의 수 중 입력되지 않은 수 두개를 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    L = [0 for _ in range(30 + 1)]
    for i in range(28):
        L[int(input())] = 1
    for i in range(1,31,1):
        if L[i] == 0:
            print(i)

if __name__ == "__main__":
    main()
