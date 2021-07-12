# Задание №3 - сделано
figure_choice = input('1 is a triangle 2 is a square, select figure:')
base = int(input('The base of the figure is: '))
height = int(input('The height of the figure is: '))


def task_3(figure_choice, base, height):
    if figure_choice == '1':
        return 0.5*base*height
    else:
        return base*height


print(task_3(figure_choice, base, height))
