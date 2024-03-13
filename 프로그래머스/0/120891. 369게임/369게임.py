def solution(order):
    str_order = str(order)
    answer = str_order.count("3")+str_order.count("6")+str_order.count("9")
    return answer