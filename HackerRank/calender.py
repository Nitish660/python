from datetime import datetime

# Input date in the format: month day year
input_date = input().strip()

# Convert the input date to a datetime object
date_obj = datetime.strptime(input_date, "%m %d %Y")

# Get the day of the week as an integer (0 = Monday, 6 = Sunday)
day_of_week = date_obj.weekday()

# List of days of the week
days_of_week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

# Output the day of the week in capital letters
print(days_of_week[day_of_week])
