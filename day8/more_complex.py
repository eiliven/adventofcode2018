
def process_children(rest, n):
    sums = ['x']
    pos = 0
    for i in range(n):
        s, p = process_node(rest[pos:])
        sums.append(s)
        pos += p
    return sums, pos


# A metadata entry of 0 does not refer to any child node.
def process_node(rest):
    child_node_count, meta_entry_count = rest[:2]
    if child_node_count == 0:
        end_pos = 2 + meta_entry_count
        return sum(rest[2:end_pos]), end_pos
    else:
        child_sums, children_end_pos = process_children(rest[2:], child_node_count)
        end_pos = 2 + children_end_pos + meta_entry_count
        smz = sum([child_sums[_] for _ in rest[2+children_end_pos:end_pos] if _ < len(child_sums) and _ != 0])
        return smz, end_pos


def to_int_list(s):
    return [int(_) for _ in s.split(' ')]


with open('input.txt') as f:
    license_txt = f.read()

print(process_node(to_int_list(license_txt)))
