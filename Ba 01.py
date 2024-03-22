from datetime import datetime, timedelta

def print_tomorrow_date():
    day = int(input("Enter the day: "))
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))

    today = datetime(year, month, day)
    tomorrow = today + timedelta(days=1)

    print(f"Tomorrow's date is: Day: {tomorrow.day}, Month: {tomorrow.month}, Year: {tomorrow.year}")


if __name__ == "__main__":
    print_tomorrow_date()