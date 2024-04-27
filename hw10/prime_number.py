def is_prime(number):
    if number <= 1:
        return f'Do not try to fool me, enter number from 2 to 1000 inclusive'
    if number >= 1001:
        return f'Do not try to fool me, enter number from 2 to 1000 inclusive'
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    else:
        return True


print(is_prime(int(input(" Enter number from 2 to 1000 inclusive: "))))



