"""
* Project : Baekjoon Online Judge Problem-2805
* Program Purpose and Features :
* - tree cutting
* Author : JH KIM
* First Write Date : 2023.09.20
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.09.20      v1.00       First Write
"""


def main():
    N, M = map(int, input().split(sep=" "))

    treeL = list(map(int, input().split(sep=" ")))
    left = 1
    right = max(treeL)
    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in range(len(treeL)):
            if treeL[i] > mid:
                total += treeL[i] - mid
        if total >= M:
            left = mid + 1
        else:
            right = mid - 1
    print(right)


if __name__ == "__main__":
    main()
