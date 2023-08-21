from google_calendar_client import GoogleCalendarClient
from webdriver_date_scrapper import get_schedule

timezone = "US/Eastern"
calendar_name = "USA Basketball"
calendar_id = ""
calendar_client = GoogleCalendarClient(timezone)

if calendar_name in calendar_client.calendars:
    calendar_id = calendar_client.calendars[calendar_name]
    print(f"{calendar_name} calendar already exists.")
else:
    calendar_id = calendar_client.create_calendar("USA Basketball")
    print(f"Created {calendar_name} calendar.")
    
    schedule = get_schedule(timezone)
    for event in schedule:
        calendar_client.create_event(calendar_id, event["name"], event["date"], event["date"])
