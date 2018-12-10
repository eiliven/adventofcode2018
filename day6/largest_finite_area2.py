import numpy as np

test_coords = [
    [1, 1],
    [1, 6],
    [8, 3],
    [3, 4],
    [5, 5],
    [8, 9]]

def relative_xy(dist):
    r = [[dist, 0], [-dist, 0], [0, dist], [0, -dist]]
    for i in range(1, dist):
        r.append([i, dist-i])
        r.append([i, -dist+i])
        r.append([-i, dist-i])
        r.append([-i, -dist+i])
    return [np.array(_) for _ in r]


with open('input.txt') as f:
    test_coords = [[int(_.strip()) for _ in r.split(',')] for r in f.readlines()]

coords = [np.array(xy) for xy in test_coords]

max_x = max_y = 0
min_x = min_y = 10000000000

for xy in coords:
    max_x = max(max_x, xy[0])
    min_x = min(min_x, xy[0])
    max_y = max(max_y, xy[1])
    min_y = min(min_y, xy[1])


both = [[xy, 1, i, True] for i, xy in enumerate(coords)]

max_x = max_x + 100
max_y = max_y + 100
distances = np.zeros(shape=(max_x, max_y), dtype=int)
owner = np.zeros(shape=(max_x, max_y), dtype=int)

# add each position as -1
for xyt in both:
    xy = xyt[0]
    distances[xy[0], xy[1]] = -1
    owner[xy[0], xy[1]] = xyt[2]


def add_it(ft, d, dxy):
    f = ft[0]
    is_done = True
    for rxy in dxy:
        c = f + rxy
        if 0 <= c[0] < max_x and 0 <= c[1] < max_y:
            if distances[c[0], c[1]] == 0:
                distances[c[0], c[1]] = d
                owner[c[0], c[1]] = ft[2]
                ft[1] += 1
                is_done = False
            elif distances[c[0], c[1]] == d:
                if owner[c[0], c[1]] != 0:
                    both[owner[c[0], c[1]]][1] -= 1  # added one before we knew it was clashing
                    owner[c[0], c[1]] = 0
        else:
            ft[3] = False
    return is_done


def find_max_area():
    # iterate outwards as long as the finite ones can still expand
    prev = 0
    next_dist = both
    for d in range(1, 150):
        print(d)
        now = next_dist
        next_dist = []
        dxy = relative_xy(d)
        #print(now)
        for f in now:
            is_done = add_it(f, d, dxy)
            if not is_done:
                next_dist.append(f)

        m = max([_[1] for _ in both if _[3]])
        #print(f'{d} {m}')
        if m == prev:
            break
        prev = m
    return m


print(distances.T)
print('Owner')
print(owner.T)
print(find_max_area())
#
# t = np.zeros((20, 20))
# for d in range(1, 10):
#     for xy in relative_xy(d):
#         t[xy[0]+10, xy[1] + 10] = d
#
#
# print(t)
