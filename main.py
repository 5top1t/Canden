from google_calendar_client import GoogleCalendarClient
from webdriver_date_scrapper import get_schedule

timezone = "US/Eastern"

# calendar_client = GoogleCalendarClient(timezone)
# team_usa_calendar_id = calendar_client.create_calendar("USA Basketball")
# print(calendar_client.calendars)

schedule = get_schedule(timezone)
for event in schedule:
    # calendar_client.create_event(team_usa_calendar_id, "USA Basketball", event_date, event_date)
    print(event)