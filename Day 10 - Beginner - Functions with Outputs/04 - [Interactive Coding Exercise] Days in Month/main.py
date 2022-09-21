def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        month_days[1] = 29
        month = month_days[month - 1]
        return month
    elif month > 12:
        return "Please pick a valid month."
    else:
        month = month_days[month - 1]
        return month
  
#🚨 Do NOT change any of the code below 
years = int(input("Enter a year: "))
months = int(input("Enter a month: "))
days = days_in_month(years, months)
print(days)