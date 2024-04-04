first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


my_list = list(first) + list(second)
my_set = set(my_list)
my_set_l = list(set(my_list))
my_set_1 = my_set_l.sort()
print(f'My list of unique elements {my_set_l}')
