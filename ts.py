from datetime import date, timedelta, datetime

def wednesday():
    dt = date.today()
    if dt.weekday() == 2:
        return dt
    elif dt.weekday() == 0:
        return date.today() + timedelta(days=2)
    elif dt.weekday() == 1:
        return date.today() + timedelta(days=1)
    elif dt.weekday() == 3:
        return date.today() + timedelta(days=6)
    elif dt.weekday() == 4:
        return date.today() + timedelta(days=5)
    elif dt.weekday() == 5:
        return date.today() + timedelta(days=4)
    elif dt.weekday() == 6:
        return date.today() + timedelta(days=3)


