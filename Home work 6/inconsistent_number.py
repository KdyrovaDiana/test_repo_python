numbers = [1, 2, 3, 4, 5, 6, 8, 9, 10]

idx = 0

while len(numbers) >= idx:
    if numbers[idx] + 1 != numbers[idx + 1]:
        print(f'{numbers[idx] + 1} is first inconsistent element in numbers {numbers[idx + 1]}')
        break
    idx += 1
else:
    print(f'{numbers} list is inconsistent')
