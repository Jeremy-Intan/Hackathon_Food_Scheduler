import datetime

def timeNow():
    somedate = datetime.datetime.today()
    month = datetime.date.today().month
    day = datetime.date.today().day
    weekday = datetime.date.today().weekday()
    hours = datetime.datetime.now().hour
    time = [[month/12, day/31, weekday/7, hours/24]]
    return time
print(timeNow())
