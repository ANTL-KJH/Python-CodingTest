def solution(arr, queries):
    for i in range(len(arr)):
        for j in range(len(queries)):
            s, e = queries[j][0], queries[j][1]
            if i>=s and i<=e:
                arr[i]+=1
    return arr