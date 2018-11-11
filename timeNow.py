import datetime

def timeNow():
    somedate = datetime.datetime.today()
    month = datetime.date.today().month
    day = datetime.date.today().day
    weekday = datetime.date.today().weekday()
    hours = datetime.datetime.now().hour
    time = [[month, day, weekday + 1, hours]]
    return time

#print(timeNow())
