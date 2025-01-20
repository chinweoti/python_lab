def is_weekday(day):
  if day == 0 or day == 6:
    return False
  return True
  
def alarm_clock(day, vacation):
  weekday = is_weekday(day)
  if vacation:
    if weekday:
      return '10:00'
    return 'off'
  else:
    if weekday:
      return '7:00'
    return "10:00"