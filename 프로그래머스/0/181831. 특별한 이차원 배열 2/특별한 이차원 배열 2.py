def check(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

def solution(arr):
    return check(arr)