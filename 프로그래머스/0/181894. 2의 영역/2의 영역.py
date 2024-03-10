def solution(arr):
    if 2 not in arr:
        answer = [-1]
    else:
        answer = arr[arr.index(2):len(arr)-arr[::-1].index(2)]
    return answer