def solution(id_pw, db):
    answer = ''
    for db_id_pw in db:
        if db_id_pw[0] == id_pw[0]:
            if db_id_pw[1] == id_pw[1]:
                answer = "login"
            else:
                answer = "wrong pw"
    if answer == '':
        answer = "fail"
    
    return answer