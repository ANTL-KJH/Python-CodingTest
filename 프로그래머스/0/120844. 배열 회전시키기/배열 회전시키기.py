def solution(numbers, direction):
    if direction == "right":
        numbers.insert(0,numbers.pop())
    elif direction == "left":
        numbers.insert(len(numbers),numbers.pop(0))
    return numbers