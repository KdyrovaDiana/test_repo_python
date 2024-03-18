course_usd = 38.45  # exchange rate of the USD to the UAH
course_eur = 42.00  # exchange rate of the EUR to the UAH

#  we ask the user for amount he wants to exchange
suma = float(input("Enter the amount you want to exchange: "))
# we ask the user for the course
valuta_1 = input("I want to exchange: ")

# we ask the user for the valuta100
valuta_2 = input("I want to get: ")


if valuta_1 == "USD" and valuta_2 == "UAH":
    convertacia = round(suma * course_usd, 2)
    print(suma, valuta_1, "=", convertacia, valuta_2)
elif valuta_1 == "EUR" and valuta_2 == "UAH":
    convertacia = round(suma * course_eur, 2)
    print(suma, valuta_1, "=", convertacia, valuta_2)
elif valuta_1 == "UAH" and valuta_2 == "USD":
    convertacia = round(suma / course_usd, 2)
    print(suma, valuta_1, "=", convertacia, valuta_2)
elif valuta_1 == "UAH" and valuta_2 == "EUR":
    convertacia = round(suma / course_eur, 2)
    print(suma, valuta_1, "=", convertacia, valuta_2)
else:
    print("error")
