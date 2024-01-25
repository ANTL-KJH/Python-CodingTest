"""
* Project Name : Baekjoon Online Judge #24060(알고리즘 수업 - 병합 정렬 1)
* Program Purpose and Basic Features :
* - 병합정렬에서 K번째 저장되는 수를 출력하는 프로그램
* Program Author : JHKIM
* Date of Original Creation : 2024.01.25
* ==========================================================================
* Program History
* ==========================================================================
* Author    	Date		    Version		Content
* JHKIM			2024.01.25	    v1.0	    First Write
"""
import sys

K = 0
cnt = 0

def mergeSort(A, N):
    return _mergeSort(A, 0, N - 1)


def _mergeSort(A, l, r):
    res = 0
    if l < r:
        mid = (l + r) // 2
        _mergeSort(A, l, mid)
        _mergeSort(A, mid + 1, r)
        merge(A, l, mid, r)



def merge(A, l, mid, r):
    left_part = A[l:mid + 1]
    right_part = A[mid + 1:r + 1]

    i = j = 0
    k = l
    global K
    global cnt
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            A[k] = left_part[i]
            i += 1
        else:
            A[k] = right_part[j]
            j += 1
        cnt += 1
        if cnt == K:
            print(A[k])
        k += 1

    while i < len(left_part):
        A[k] = left_part[i]
        i += 1
        cnt += 1
        if cnt ==K:
            print(A[k])
        k += 1



    while j < len(right_part):
        A[k] = right_part[j]
        j += 1
        cnt += 1
        if cnt ==K:
            print(A[k])
        k += 1


def main():
    global K, cnt
    N, K = map(int, sys.stdin.readline().rstrip().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))

    mergeSort(A, N)
    if cnt < K:
        print(-1)


if __name__ == "__main__":
    main()
