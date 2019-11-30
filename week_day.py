import datetime
import calendar

def day():
  weekday = datetime.date.today().weekday()
  weekday_name = calendar.day_name[weekday]

  return weekday_name
  