from home_work_11.mathematics.calculator.correct_symbols.correct_symbols import check_user_choice
from home_work_11.mathematics.mathematics import temperature_f_to_c, temperature_c_to_f


def converter_t(operation, temperature):
    if operation == 'f':
        res = temperature_f_to_c(temperature)
        print(f'Fahrenheit {temperature} = Celsius {res}')
    elif operation == 'c':
        res = temperature_c_to_f(temperature)
        print(f'Celsius {temperature} = Fahrenheit {res}')
    else:
        raise ValueError("Incorrect temperature")
    return res


def run_convert_t(operation):
    operation = check_user_choice(operation)
    try:
        temperature = float(input("Enter temperature: "))
    except ValueError:
        temperature = float(input("Incorrect temperature. Enter temperature: "))
    result = converter_t(operation, temperature)
    return result