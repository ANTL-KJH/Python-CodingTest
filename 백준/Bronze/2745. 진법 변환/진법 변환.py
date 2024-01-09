"""
* Project Name : Baekjoon Online Judge #2745(진법 변환)
* Program Purpose and Basic Features :
* - B진법 숫자를 10진법으로 바꿔 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.09
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.09	    v1.0	    First Write
"""


def main():
    N, B = input().split()
    B = int(B)
    result = 0
    for i in range(len(N)):
        if N[i] >= 'A' and N[i] <= 'Z':
            result += (ord(N[i]) - ord('A') + 10) * pow(B, len(N) - (i + 1))
        else:
            result += int(N[i]) * pow(B, len(N) - (i + 1))
    print(result)


if __name__ == "__main__":
    main()
