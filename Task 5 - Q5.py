from datetime import datetime

dt = datetime(2028, 12, 31)

#To extract year, month and day
extract_date = lambda dt: (dt.year, dt.month, dt.day)
year,month,day = extract_date(dt)

# To print
print(f"Year: {year}, Month: {month}, Day: {day}")