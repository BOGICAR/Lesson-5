# Задание №7 - сделано
import datetime


print('Enter day, month, year in the format: dd.mm.yyyy')
input_d_m_y = input('Enter the day: ')


def is_date():
    try:
        valid_time = datetime.datetime.strptime(input_d_m_y, '%d.%m.%Y')
        conv_valid_time = bool(valid_time.strftime('%d.%m.%Y'))
    except:
        print('False')
    return conv_valid_time


print(is_date())
