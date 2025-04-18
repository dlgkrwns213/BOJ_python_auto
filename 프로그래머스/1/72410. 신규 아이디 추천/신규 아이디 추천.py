def solution(new_id):
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step34(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)
    return new_id

def step1(id):
    return id.lower();

def step2(id):
    new_id_list = []
    for x in id:
        if x.islower() or x.isnumeric() or x in '-_.':
            new_id_list.append(x)
    return ''.join(new_id_list)

def step34(id):
    new_id_list = id.replace('.', ' ').split()
    return '.'.join(new_id_list)

def step5(id):
    return id if id else 'a'

def step6(id):
    return id[:15].replace('.', ' ').strip().replace(' ', '.')

def step7(id):
    return id + id[-1] * (max(3-len(id), 0))
    

    