
def process_children(rest, n):
    total = pos = 0
    for i in range(n):
        s, p = process_node(rest[pos:])
        total += s
        pos += p
    return total, pos


def process_node(rest):
    child_node_count, meta_entry_count = rest[:2]
    child_sum, child_end_pos = process_children(rest[2:], child_node_count)
    end_pos = 2 + child_end_pos + meta_entry_count
    return child_sum + sum(rest[2+child_end_pos:end_pos]), end_pos


def to_int_list(s):
    return [int(_) for _ in s.split(' ')]


with open('input.txt') as f:
    license_txt = f.read()

print(process_node(to_int_list(license_txt)))
