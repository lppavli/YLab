import itertools


def p(sp):
    r = 1
    for i in sp:
        r *= int(i)
    return r


def count_1(pr_i, limit):
    dl = 1
    sp = 0
    while dl < limit:
        dl *= pr_i
        sp += 1
    return sp


def count_find_num(pr, limit):
    res = []
    d = {str(pr_i): count_1(pr_i, limit) for pr_i in pr}
    n = p(pr)
    z = (itertools.product(' '.join([str(i) for i in range(1, d[str(pr[0])])]).split(), repeat=len(pr)))
    z_res = filter(lambda x: (x.count(i) <= d[i] for i in d.keys()), z)
    for i in z_res:
        numb = p((a ** int(b) for a, b in zip(pr, i)))
        if numb <= limit:
            res.append(numb)

    return [len(set(res)), max(res)] if res else []
