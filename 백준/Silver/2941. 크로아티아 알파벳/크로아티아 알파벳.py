"""
* Project Name : Baekjoon Online Judge #2941(크로아티아 알파벳)
* Program Purpose and Basic Features :
* - 크로아티아 알파벳이 주어졌을 때 몇개의 크로아티아 알파벳으로 이루어져 있는지 구하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    s = input()
    for i in c_alpha:
        s = s.replace(i, '*')
    print(len(s))


if __name__ == "__main__":
    main()
