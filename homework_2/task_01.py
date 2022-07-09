import itertools


# https://github.com/mnv/python-basics


def get_dist(point_1, point_2):
    res = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
    return res


points = [(0, 2), (2, 5), (8, 3), (5, 2), (6, 6)]
a = list(itertools.permutations(points[1:]))
current = points[0]
minim = 1000000000000000000000

for item in a:
    res = {}
    dist = 0
    item = list(item)
    item.insert(0, current)
    for i in range(1, len(item)):
        dist += get_dist(item[i - 1], item[i])
        res[item[i]] = dist
    dist += get_dist(current, item[i])
    res[current] = dist
    if dist < minim:
        minim_res = res
        minim = dist
print(current, end=" ")
for k, v in minim_res.items():
    print(f"-> {k}[{v}]", end=" ")
print("=", minim_res[current])
