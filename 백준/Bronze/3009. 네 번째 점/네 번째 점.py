"""
* Project Name : Baekjoon Online Judge #3009(네 번째 점)
* Program Purpose and Basic Features :
* - 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.10
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.10	    v1.0	    First Write
"""


def main():
    xL = []
    yL = []
    for _ in range(3):
        x, y = map(int, input().split())
        xL.append(x)
        yL.append(y)
    x, y = 0, 0
    for i in range(3):
        if xL.count(xL[i]) % 2 != 0:
            x = xL[i]
        if yL.count(yL[i]) % 2 != 0:
            y = yL[i]
    print(x,y)


if __name__ == "__main__":
    main()
