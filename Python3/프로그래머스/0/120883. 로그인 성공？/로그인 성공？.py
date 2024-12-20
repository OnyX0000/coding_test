def solution(id_pw, db):
    answer = ''
    db_dict = dict(db)
    ide = id_pw[0]
    pw = id_pw[1]
    
    if ide in db_dict :
        if pw == db_dict[ide] :
            return 'login'
        else:
            return 'wrong pw'
    else:
        return 'fail'