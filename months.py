# months.py

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def month(n: int) -> str:
    """Return the month name for month number n (1..12)."""
    if 1 <= n <= 12:
        return MONTHS[n - 1]
    raise ValueError("Month number must be from 1 to 12.")
