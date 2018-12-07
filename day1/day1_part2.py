
with open('input.txt') as f:
    frequency_changes = f.readlines()

seen = {}
current_frequency = 0
repeated = False
while not repeated:
    for change in frequency_changes:
        seen[current_frequency] = True
        current_frequency += int(change)
        if current_frequency in seen:
            repeated = True
            break
print(current_frequency)
