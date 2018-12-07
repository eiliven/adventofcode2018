import numpy as np
from collections import namedtuple

Area = namedtuple('Area', ['x', 'y', 'w', 'h', 'the_id'])


def parse_claim(c):
    the_id, b = c.split('@')
    x_y, w_h = b.split(':')
    x, y = x_y.strip().split(',')
    w, h = w_h.strip().split('x')
    return Area(int(x), int(y), int(w), int(h), the_id)


with open('input.txt') as f:
    claims = f.readlines()

max_x = max_y = 0
areas = []
for claim in claims:
    a = parse_claim(claim)
    max_x = max(max_x, a.x + a.w)
    max_y = max(max_y, a.y + a.h)
    areas.append(a)

total = np.zeros((max_x, max_y))
mas = []
# stupidly inefficient!!!! but what can you do...
for a in areas:
    ma = np.zeros((max_x, max_y))
    mas.append((ma, a))
    for wi in range(a.w):
        for hj in range(a.h):
            mx = a.x + wi
            my = a.y + hj
            total[mx, my] += 1
            ma[mx, my] += 1

for ma, a in mas:
    min_x = a.x
    max_x = a.x + a.w
    min_y = a.y
    max_y = a.y + a.h
    if np.sum(total[min_x:max_x, min_y:max_y] - ma[min_x:max_x, min_y:max_y]) == 0:
        print(a.the_id)
        break
