def solution(numbers, k):
    for i in range(k-1):
        numbers.insert(len(numbers),numbers.pop(0))
        numbers.insert(len(numbers),numbers.pop(0))
    answer = numbers[0]
    return answer