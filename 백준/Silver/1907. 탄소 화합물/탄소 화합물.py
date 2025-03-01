atom_weight = {'C': 1, 'H': 1 << 8, 'O': 1 << 16}


def break_element(element: str):
    ret, idx = 0, 0
    while idx < len(element):
        atom = element[idx]
        plus = 1
        if idx + 1 < len(element) and element[idx+1].isdigit():
            plus = int(element[idx+1])
            idx += 2
        else:
            idx += 1

        ret += plus * atom_weight[atom]

    return ret


def calculate(ar, br, cr):
    for x in range(1, 11):
        for y in range(1, 11):
            for z in range(1, 11):
                if x * ar + y * br == z * cr:
                    return x, y, z
    return -1, -1, -1


ab, c = input().split('=')
a, b = ab.split('+')

print(*calculate(break_element(a), break_element(b), break_element(c)))