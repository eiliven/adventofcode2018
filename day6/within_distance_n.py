import numpy as np


def max_min(arr, idx):
    return arr[:, idx].max(), arr[:, idx].min()


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def total_dist(p):
    return np.apply_along_axis(lambda _: manhattan_dist(p, _), axis=1, arr=the_places).sum()


def count_larger(arr, n):
    return np.where(arr < n, 1, 0).sum()


with open('input.txt') as f:
    test_coords = [[int(_.strip()) for _ in r.split(',')] for r in f.readlines()]

the_places = np.array([np.array(xy) for xy in test_coords])
max_x, min_x, = max_min(the_places, 0)
max_y, min_y = max_min(the_places, 1)

# it would be smarter to circle outwards and stop when we are far away...
area = np.zeros(shape=(max_x, max_y), dtype=int)
for x in range(0, max_x):
    for y in range(0, max_y):
        area[x, y] = total_dist([x, y])

print(count_larger(area, 10000))
