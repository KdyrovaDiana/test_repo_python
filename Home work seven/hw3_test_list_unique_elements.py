numbers = input("Enter numbers: ").split()
my_set = set(numbers)
if len(numbers) == len(my_set):
    print(f'The list {numbers} consists of unique elements')
else:
    print(f'There are duplicates in the list {numbers}')
