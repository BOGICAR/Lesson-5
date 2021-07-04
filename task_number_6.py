# Задание №6 - сделано
def task_6():
    dictionary_1 = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
    new_dictionary = {k: v for k, v in dictionary_1.items() if v is not None}
    return new_dictionary


print(task_6())
