

# couldn't be asked implementing this, got it from the interwebs
# https://stackoverflow.com/questions/2460177/edit-distance-in-python
def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


with open('input.txt') as f:
    box_ids = f.readlines()

for bid1 in box_ids:
    for bid2 in box_ids:
        d = levenshtein_distance(bid1, bid2)
        if d == 1:
            break
    else:
        continue  # only executed if the inner loop did NOT break
    break  # only executed if the inner loop DID break

print(f'{bid1} {bid2}')
same = ''.join([bid1[i] for i in range(len(bid1)) if bid1[i] == bid2[i]])
print(f'{same}')
