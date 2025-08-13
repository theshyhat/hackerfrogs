# URL
https://hack.arrrg.de/challenge/76
# category
programming
# concept
* calculate the time between one date and the current date
* the challenge wants to know how many minutes have elapsed since we registered on the website
# method of solve
* there a website we can use to calculate the number of minutes since a specific date
```
https://www.timeanddate.com
```
* we could also use a Python script to calculate the number of elapsed minutes:
```
from datetime import datetime

# Define the reference date
reference_date_str = "2025-06-03 02:50:00"
reference_date = datetime.strptime(reference_date_str, "%Y-%m-%d %H:%M:%S")

# Get the current date and time
current_date = datetime.now()

# Calculate the time difference (timedelta object)
time_difference = current_date - reference_date

# Convert the timedelta to total minutes
minutes_since_date = time_difference.total_seconds() / 60

print(f"Minutes since {reference_date_str}: {minutes_since_date:.2f}")
```
* an important thing to note when we do the calculations is that the server we're sending tht answer to is in Germany
* so if we are in the PST timezone (West Coast North America), then difference in time is 8 or 9 hours (depending on Daylight Savings Time),
* if the difference is 9 hours, then we have to add 560 minutes (9 x 60)
