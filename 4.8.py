

def time_string(hours, minutes, time_format):
    result = ' '
    if time_format == '24':
        result = (f'{hours}:{minutes}')
    elif time_format == '12' and hours > 12:
        result = (f'{hours - 12}:{minutes}PM')
    elif time_format == '12':
        result = (f'{hours}:{minutes}PM')
hours = int(input('Input hour: '))
minutes = int(input('Input minutes: '))
time_format = int(input('Input Time format: '))
date = time_string(hours, minutes, time_format)
print(date)