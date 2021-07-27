from datetime import datetime


def Time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def Date_For_Excel_File():
    Year = datetime.now().year
    Month = datetime.now().month
    Date = f'{Month}_{Year}'
    return Date


def Date():
    Date = datetime.today().strftime('%Y-%m-%d')
    return Date


def Day():
    Date = datetime.today().strftime("%A")
    return Date


def Month():
    Date = datetime.today().strftime("%B")
    return Date
