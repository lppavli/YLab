import itertools, functools


def multiple(sp):
    return functools.reduce(lambda result, element: result * element, sp)


def count_1(pr_i, limit):
    dl = 1
    sp = 0
    while dl < limit:
        dl *= pr_i
        sp += 1
    return sp


def count_find_num(pr, limit):
    res = []
    d = {pr_i: count_1(pr_i, limit) for pr_i in pr}
    d_iter = []
    for k, v in d.items():
        a = list(itertools.product([k], range(1, v + 1)))
        d_iter.append(a)
    combinations = itertools.product(*d_iter)
    for item in combinations:
        numb = multiple((n ** degree for n, degree in item))
        if numb <= limit:
            res.append(numb)
    return [len(set(res)), max(res)] if res else []
