import random

pull_count = 100000
overall_count = []
count_is_1 = 0
count_is_2 = 0
count_is_3 = 0

for i in range(pull_count):
    deck = []
    group = []

    draw1 = random.randint(0, 5)
    if draw1 in [0, 1]:
        group.append('a')
    elif draw1 in [2, 3]:
        group.append('b')
    elif draw1 in [4, 5]:
        group.append('c')
    deck.append(draw1)

    draw2 = random.randint(0, 5)
    if (draw2 in [0, 1] and 'a' in group) or (draw2 in [2, 3] and 'b' in group) or (draw2 in [4, 5] and 'c' in group):
        draw2 = (draw2 + random.randint(1, 5)) % 6
    if draw2 in [0, 1]:
        group.append('a')
    elif draw2 in [2, 3]:
        group.append('b')
    elif draw2 in [4, 5]:
        group.append('c')
    deck.append(draw2)
    
    draw3 = random.randint(0, 5)
    if (draw3 in [0, 1] and 'a' in group) or (draw3 in [2, 3] and 'b' in group) or (draw3 in [4, 5] and 'c' in group):
        draw3 = (draw3 + random.randint(1, 5)) % 6
    if draw3 in [0, 1]:
        group.append('a')
    elif draw3 in [2, 3]:
        group.append('b')
    elif draw3 in [4, 5]:
        group.append('c')
    deck.append(draw3)

    unique_group_count = len(set(group))
    overall_count.append(unique_group_count)
    if unique_group_count == 1:
        count_is_1 += 1
    if unique_group_count == 2:
        count_is_2 += 1
    if unique_group_count == 3:
        count_is_3 += 1

print(count_is_1)
print(count_is_2)
print(count_is_3)

print(count_is_1/pull_count)
print(count_is_2/pull_count)
print(count_is_3/pull_count)
