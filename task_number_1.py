# Задание №1 - сделано
def user_input():
    u_input = int(input('Enter a number between 0 and 1000: '))
    return u_input


def is_prime(user_input):
    number_of_attempts = 0
    if 1001 > user_input > 1:
        for i in range(1, user_input + 1):
            perebor = user_input % i
            if perebor == 0:
                number_of_attempts += 1
        if number_of_attempts > 2:
            print('False')
        else:
            print('True')
    else:
        print('False')


is_prime(user_input())
