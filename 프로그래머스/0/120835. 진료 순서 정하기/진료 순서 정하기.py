def solution(emergency):
    r_emergency = sorted(emergency, reverse=True)
    answer = [r_emergency.index(i)+1 for i in emergency]
    return answer