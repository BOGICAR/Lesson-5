# Задание №3 - сделано
def task_3():
    figure_choice = input('1 is a triangle 2 is a square, select figure:')
    area = 0
    if figure_choice == '1':
        base = int(input('The base of the triangle is: '))
        height = int(input('The height of the triangle is: '))
        area = 0.5*base*height
    elif figure_choice == '2':
        side = int(input('The side of the square is: '))
        area = side**2
    else:
        print('Please select 1 or 2 and try again')
    return area


print(task_3())