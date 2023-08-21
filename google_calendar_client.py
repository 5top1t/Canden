from google.auth.exceptions import RefreshError
from googleapiclient import sample_tools

class GoogleCalendarClient:
    
    def __init__(self, timezone) -> None:
        self.service, self.flags = sample_tools.init(
            [],
            "calendar",
            "v3",
            __doc__,
            __file__,
            scope="https://www.googleapis.com/auth/calendar",
        )
        self.timezone = timezone
        self.calendars = {}
        self._get_all_calendars()
        
    def create_event(self, calendar_id, summary, startDate, endDate):
        date_format = "%Y-%m-%d"
        event = {
            'summary': summary, 
            'location': '',
            'description': '',
            'start': {
                'date': startDate.strftime(date_format),
                'timeZone': self.timezone,
            },
            'end': {
                'date': endDate.strftime(date_format),
                'timeZone': self.timezone,
            },
            'recurrence': [],
            'attendees': [],
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        event = self.service.events().insert(calendarId=calendar_id, body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
                
    def create_calendar(self, calendar_name):
        calendar = {
            'summary': calendar_name,
            'timeZone': self.timezone
        }

        created_calendar = self.service.calendars().insert(body=calendar).execute()
        self._insert_calendar(created_calendar)
        return created_calendar.get("id")

    def _get_all_calendars(self):
        try:
            page_token = None
            while True:
                calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
                for calendar_list_entry in calendar_list["items"]:
                    self._insert_calendar(calendar_list_entry)    
                page_token = calendar_list.get("nextPageToken")
                if not page_token:
                    break

        except RefreshError:
            print(
                "The credentials have been revoked or expired, please re-run"
                "the application to re-authorize."
            )
            

    def _insert_calendar(self, calendar):
        self.calendars[calendar["id"]] = calendar["summary"]