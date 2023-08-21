from datetime import datetime
from selenium import webdriver 
from bs4 import BeautifulSoup
import pytz

# Create Chrome options with headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Enable headless mode
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.usab.com/teams/5x5-mens-world-cup/schedules" 
driver.get(url) 


def get_schedule(timezone):
    event_dates = []
    
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        schedule_list = soup.find_all('div', class_='border')

        if schedule_list:
            for event_entry in schedule_list:
                event_date = _get_event_date(event_entry, timezone)
                event_dates.append(event_date)
        else:
            print("No schedule table found on the page.")
    finally:
        driver.quit()
        return event_dates 
    
def _get_event_date(event_entry, timezone):
    month_text = event_entry.find('time', class_='uppercase').get_text()
    day_text = event_entry.find('time', class_='days').get_text()
                
    # Events in the past have no time element
    time_element = event_entry.find('span', class_='uppercase')
    time_text = time_element.get_text() if time_element else ""
    
    event_date = _parse_datetime(month_text, day_text, datetime.now().year, time_text, timezone)
    
    return event_date

    
def _parse_datetime(month, day, year, time, timezone):
    if not time:
        time = "12:00 AM EST"
    
    event_date_format = f"{month} {day} {year} {time}"
    full_format = "%b %d %Y %I:%M %p %Z"
   
    try: 
        dt_object = datetime.strptime(event_date_format, full_format)
        timezone = pytz.timezone(timezone)
        dt_object = timezone.localize(dt_object)
        return dt_object
    except ValueError:
        print(ValueError(f"Unable to parse datetime string: {event_date_format}"))
        return None