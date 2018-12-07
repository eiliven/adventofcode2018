# counting the number that have an ID containing exactly two of any letter and
# then separately counting those with exactly three of any letter.
# You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.
from collections import defaultdict

with open('input.txt') as f:
    box_ids = f.readlines()

# test
# box_ids = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

twos = 0
threes = 0
for bid in box_ids:
    letter_count = defaultdict(int)
    had_three = had_two = False
    for l in bid:
        letter_count[l] += 1
    for countz in letter_count.values():
        if countz == 2:
            had_two = True
        if countz == 3:
            had_three = True
    if had_two:
        twos += 1
    if had_three:
        threes += 1

print(f'{twos} * {threes} = {twos * threes}')
