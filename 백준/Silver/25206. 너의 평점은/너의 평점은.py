"""
* Project Name : Baekjoon Online Judge #25206(너의 평점은)
* Program Purpose and Basic Features :
* - 전공평점을 계산하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.08
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.08	    v1.0	    First Write
"""


def main():
    gradeName = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
    score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]
    totalCredit = 0
    totalGrade = 0
    for i in range(20):
        subject, credit, grade = input().split()
        credit = float(credit)
        grade = grade
        if grade == "P":
            continue
        else:
            totalGrade += score[gradeName.index(grade)] * credit
            totalCredit += credit
    print("{}".format(totalGrade/totalCredit))

if __name__ == "__main__":
    main()
