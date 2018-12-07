import numpy as np
from collections import namedtuple

# test
# claims = [
# '#1 @ 1,3: 4x4',
# '#2 @ 3,1: 4x4',
# '#3 @ 5,5: 2x2']

Area = namedtuple('Area', ['x', 'y', 'w', 'h'])


def parse_claim(c):
    ignore, b = c.split('@')
    x_y, w_h = b.split(':')
    x, y = x_y.strip().split(',')
    w, h = w_h.strip().split('x')
    return Area(int(x), int(y), int(w), int(h))


with open('input.txt') as f:
    claims = f.readlines()

max_x = max_y = 0
areas = []
for claim in claims:
    a = parse_claim(claim)
    max_x = max(max_x, a.x + a.w)
    max_y = max(max_y, a.y + a.h)
    areas.append(a)

mz = np.zeros((max_x, max_y))
# stupidly inefficient, but what can you do
for a in areas:
    for wi in range(a.w):
        for hj in range(a.h):
            mx = a.x + wi
            my = a.y + hj
            mz[mx, my] += 1

overlapping = np.where(mz > 1, 1, 0)
print(np.sum(overlapping))
