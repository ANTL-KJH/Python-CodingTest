"""
* Project : Baekjoon Online Judge Problem-1654
* Program Purpose and Features :
* - LAN cable cutting
* Author : JH KIM
* First Write Date : 2023.09.20
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.09.20      v1.00       First Write
"""


def main():
    K, N = map(int, input().split(sep=" "))

    cableL = []

    for _ in range(K):
        cableL.append(int(input()))

    left = 1
    right = max(cableL)

    while left <= right:
        mid = (left + right) // 2
        total = 0
        for i in range(len(cableL)):
            total += cableL[i] // mid

        if total >= N:
            left = mid + 1
        else:
            right = mid - 1
    print(right)


if __name__ == "__main__":
    main()
