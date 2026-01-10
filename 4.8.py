
def time_string(hours, minutes, time_format):
    if time_format == '24':
        return f"{hours:02d}:{minutes:02d}"

    if time_format == '12':
        suffix = "am" if hours < 12 else "pm"
        h12 = hours % 12
        if h12 == 0:
            h12 = 12
        return f"{h12}:{minutes:02d}{suffix}"

    raise ValueError("time_format must be '24' or '12'")
hours = int(input('Input hour (0-23): '))
minutes = int(input('Input minutes (0-59): '))
time_format = input("Input time format ('24' or '12'): ")

print(time_string(hours, minutes, time_format))