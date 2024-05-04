def check_user_choice(operation, correct_symbols=('f', 'c')):
    while operation not in correct_symbols:
        operation = input("Enter operation (Enter 'f', 'c'): ")
    return operation
