# Задание №4 - сделано
import random


def task_4():
    list_1 = []
    amount_of_added_numbers = 20
    while amount_of_added_numbers > 0:
        list_1.append(random.randrange(0, 100))
        amount_of_added_numbers -= 1
    amount_of_odd_numbers = 0
    for i, element in enumerate(list_1):
        if element % 2 != 0:
            list_1[i] = 0
            amount_of_odd_numbers += 1
        else:
            continue
    return amount_of_odd_numbers


print('Amount of add numbers:', task_4())
