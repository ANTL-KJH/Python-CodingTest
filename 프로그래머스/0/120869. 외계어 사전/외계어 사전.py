def check(spell, dic):
    for di in dic:
        cnt = 0
        for sp in spell:
            if di.count(sp)!=1:
                break
            cnt += 1
        if cnt == len(spell):
            return 1
    return 2
    
def solution(spell, dic):
    answer = check(spell,dic)
    return answer