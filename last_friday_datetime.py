import calendar

def get_last_friday(string: str) -> str:

    month, year = string.split("/")
    last_day = calendar.monthrange(int(year), int(month))[1]
    last_weekday = calendar.weekday(int(year), int(month), last_day)
    last_friday = last_day - ((7 - (4 - last_weekday)) % 7)
    
    return f"{last_friday}.{month}.{year}"


# print(get_last_friday('01/2024'))