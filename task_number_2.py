# Задание №2 - сделано
u_input = input('Enter some text: ')


def amount_words(user_input):
    user_input = len(user_input.split())
    return user_input


def amount_elements(user_input):
    return len(user_input)


print('Amount of words, elements: ', amount_words(u_input), amount_elements(u_input))
