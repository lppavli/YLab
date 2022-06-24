from itertools import product


def bananas(s) -> set:
    result = set()
    a = list(product('-*', repeat=len(s)))
    for comb in a:
        item = ''.join([s[i] if comb[i] == '*' else comb[i] for i in range(len(s))])
        if item.replace('-', '') == 'banana':
            result.add(item)
    return result


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                                "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                                "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"}
