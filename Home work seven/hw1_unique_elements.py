# 1- Version
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
my_list = []
for i in first:
    if i in my_list:
        continue
    for j in second:
        if i == j:
            my_list.append(i)
            break
print(f'My list of unique elements {my_list}. 1-Version')

# 2-Version
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
my_set_1 = set(first)
my_set_2 = set(second)
my_list = list(my_set_1.intersection(my_set_2))
print(f'My list of unique elements {my_list}. 2-Version')

