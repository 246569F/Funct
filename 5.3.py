# keyboard.py
# Functions to read any data type from the keyboard

def input_string(message: str) -> str:
    value = input(message)
    return value


def input_integer(message: str) -> int:
    while True:
        text = input(message)
        try:
            return int(text)
        except ValueError:
            print("Błąd: wpisz liczbę całkowitą (np. 25).")


def input_real(message: str) -> float:
    while True:
        text = input(message)
        # jeśli ktoś wpisze 123,45 zamiast 123.45
        text = text.replace(",", ".")
        try:
            return float(text)
        except ValueError:
            print("Błąd: wpisz liczbę rzeczywistą (np. 3500.50).")


def input_boolean(message: str) -> bool:
    while True:
        text = input(message).strip().lower()
        if text == "y":
            return True
        if text == "n":
            return False
        print("Błąd: wpisz 'y' (tak) albo 'n' (nie).")


# main.py
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed

import keyboard  # your own defined module

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name, last_name)
print('Age:', age)

if is_salary_hidden:
    print('Salary: HIDDEN')
else:
    print('Salary:', salary)
