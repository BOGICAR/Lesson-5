# Задание №6 - сделано
dictionary_1 = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}


def task_6(dictionary_1):
    new_dictionary = {k: v for k, v in dictionary_1.items() if v is not None}
    return new_dictionary


print(task_6(dictionary_1))
