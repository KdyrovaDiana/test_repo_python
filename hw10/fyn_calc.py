def calc(number1, number2, operator):
    result = None
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        if number2 == 0:
            print("Stop! You can't divide by zero")
            return
        result = number1 / number2
    else:
        print("Incorrect operation")
    return result


def operations():
    operator = input("Enter operator(Enter '+', '-', '*', '/'): ")
    correct_operations = ['+', '-', '*', '/']
    while operator not in correct_operations:
        print("Do not try to fool me, enter operator")
        operator = input("Enter operator(Enter '+', '-', '*', '/'): ")
    return operator


def run():
    try:
        number1 = float(input("Enter a first number: "))
    except ValueError:
        number1 = float(input("Do not try to fool me, enter number: "))
    try:
        number2 = float(input("Enter a second number: "))
    except ValueError:
        number2 = float(input("Do not try to fool me, enter number: "))
    operator = operations()
    result = calc(number1, number2, operator)
    print(f'Your result: {result}')


program_is_running = True
while program_is_running:
    run()
    answer = input("If you want to continue, enter '+', if no, press any other sign: ")
    if answer != '+':
        program_is_running = False
