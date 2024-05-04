from home_work_11.mathematics.calculator.calculator_tem import run_convert_t

if __name__ == '__main__':
    print('''Welcome to the currency converter! \n Select operation: \n    - Fahrenheit enter: f 
    - Celsius enter: c \n  ''')
    choice = input("What do you want to chose? ").lower()
    run_convert_t(choice)
