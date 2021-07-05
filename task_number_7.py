# Задание №7 - сделано
import datetime


print('Enter day, month, year in the format: dd.mm.yyyy')
input_d_m_y = input('Enter the day: ')
conv_valid_time = 0


def is_date(conv_valid_time):
    try:
        valid_time = datetime.datetime.strptime(input_d_m_y, '%d.%m.%Y')
        conv_valid_time = bool(valid_time.strftime('%d.%m.%Y'))
        print(conv_valid_time)
    except:
        print(bool(conv_valid_time))
    return


is_date(conv_valid_time)
