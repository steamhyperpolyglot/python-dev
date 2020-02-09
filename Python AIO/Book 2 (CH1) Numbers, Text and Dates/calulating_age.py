import datetime as dt
today = dt.date.today()
birthdate = dt.date(2000, 12, 31)
delta_age = (today - birthdate)
print(delta_age.days, type(delta_age.days))
years_old = delta_age.days // 365
print(years_old)

