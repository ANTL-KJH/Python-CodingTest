import re
def solution(my_string):
    my_string = re.sub(r'[a-zA-z]',' ', my_string)
    numL = list(map(int, my_string.split()))
    answer = sum(numL)
    return answer