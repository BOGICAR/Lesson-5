# Задание №5 - сделано
input_number = float(input())


def task_5(input_number):
    perimeter_square = input_number * 4
    square_area = input_number ** 2
    square_area_up = format(square_area, '.2f')
    diagonal_square = 2**0.5 * input_number
    diagonal_square_up = format(diagonal_square, '.2f')
    return perimeter_square, square_area_up, diagonal_square_up


print(task_5(input_number))
