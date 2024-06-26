your_list = [    ("apple", 3, 5),
    ("banana", 2, 4),    ("cherry", 1, 6)
]
sorted_list = sorted(your_list, key=lambda x: (x[2], x[1], len(x[0]), -x[1]))
print(sorted_list)


def pop():
    return None