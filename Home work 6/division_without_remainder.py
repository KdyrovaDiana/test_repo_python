numbers = [1, 4, 6, 10, 25, 29, 33, 65, 68, 99, 103, 120, 125, 159]
even_numbers = list()
my_number = int(input("Enter number: "))
for number in numbers:
    if number % my_number == 0:
        even_numbers.append(number)
print(f' {even_numbers} list elements divide by {my_number}')
