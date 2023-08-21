from google_calendar_client import GoogleCalendarClient
from webdriver_date_scrapper import get_event_dates

timezone = "US/Eastern"

calendar_client = GoogleCalendarClient(timezone)
calendar_client.create_calendar("USA Basketball")
print(calendar_client.calendars)

event_dates = get_event_dates(timezone)
for event_date in event_dates:
    calendar_client.create_event("primary", "USA Basketball", event_date, event_date)
# print(event_dates)