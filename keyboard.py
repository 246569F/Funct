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
