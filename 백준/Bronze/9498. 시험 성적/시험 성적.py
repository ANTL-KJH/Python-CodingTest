"""
* Project Name : Baekjoon Online Judge #9498(두 수 비교하기)
* Program Purpose and Basic Features :
* - 시험 점수를 입력받고 점수에 따라 성적을 출력하는 프로그램
* Program Author : JHKIM
* Date of original creation : 2024.01.04
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.04	    v1.0	    First Write
"""


def main():
    score = int(input())
    if score <=100 and score >=90:
        print("A")
    elif score < 90 and score >=80:
        print("B")
    elif score < 80 and score >= 70:
        print("C")
    elif score < 70 and score>=60:
        print("D")
    else:
        print("F")


if __name__ == "__main__":
    main()
