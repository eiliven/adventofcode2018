complete_polymer = 'dabAcCaCBAcCcaDA'


def is_reaction(a, b):
    return a != b and a.lower() == b.lower()


def react(polymer):
    rest = ''
    i = 1
    a = polymer[0]
    while i < len(polymer):
        b = polymer[i]
        if not is_reaction(a, b):
            rest += a
            a = b
            i += 1
            if i == len(polymer):
                rest += polymer[-1]
            continue
        else:
            if i < len(polymer) - 2:
                a = polymer[i+1]
            i += 2
    return rest


def recursive_reactions(polymer):
    after = polymer
    while True:
        before = after
        after = react(before)
        if before == after:
            break
    return after


with open('input.txt') as f:
    complete_polymer = f.read()

min_length = 100000000000
units = {_.lower() for _ in complete_polymer}

for unit in units:
    reduced_polymer = complete_polymer.replace(unit, '').replace(unit.upper(), '')
    after = recursive_reactions(reduced_polymer)
    print(unit, len(after))
    this_length = len(after)
    if this_length < min_length:
        min_length = this_length

print(min_length)
