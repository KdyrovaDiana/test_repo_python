first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 'test', False, 623]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'abc']

set1 = set(first)
set2 = set(second)
set3 = set1.difference(set2)
print(f'Unique elements of the first list: {set3}')
