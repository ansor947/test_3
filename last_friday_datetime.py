import datetime

from dateutil.relativedelta import FR, relativedelta
 
def last_friday(d):

    d = datetime.datetime.strptime("01/" + d, "%d/%m/%Y")
    res = d+relativedelta(day=31, weekday=FR(-1))
    return res.strftime("%d.%m.%Y")

print(last_friday('05/2022'))

    