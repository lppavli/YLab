from functools import lru_cache


@lru_cache(None)
def get_items(s, word):
    res = []
    if word == "":
        res.append("".rjust(len(s), "-"))
        return res
    for i in range(len(s)):
        if word[0] == s[i]:
            left_s = "".rjust(i, "-") + s[i]
            if s[i + 1 :] == "" and word[1:] == "":
                res.append(left_s)
            else:
                right_s_list = get_items(s[i + 1 :], word[1:])
                for right_s in right_s_list:
                    res.append(left_s + right_s)
    return res


def bananas(s) -> set:
    return set(get_items(s, "banana"))


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {
    "b-an--ana",
    "-banana--",
    "-b--anana",
    "b-a--nana",
    "-banan--a",
    "b-ana--na",
    "b---anana",
    "-bana--na",
    "-ba--nana",
    "b-anan--a",
    "-ban--ana",
    "b-anana--",
}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {
    "ban--ana",
    "ba--nana",
    "bana--na",
    "b--anana",
    "banana--",
    "banan--a",
}
