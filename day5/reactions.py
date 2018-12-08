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
            a = polymer[i+1]
            i += 2
    return rest


with open('input.txt') as f:
    complete_polymer = f.read()

after = before = complete_polymer
while True:
    before = after
    after = react(before)
    if before == after:
        break

print(len(after))
