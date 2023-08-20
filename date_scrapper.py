import requests
from bs4 import BeautifulSoup

url = "https://www.usab.com/teams/5x5-mens-world-cup/schedules"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the game schedule
    schedule_table = soup.find('table', class_='table-schedules')
    
    if schedule_table:
        # Extract information from the table rows
        rows = schedule_table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            date = columns[0].get_text()
            time = columns[1].get_text()
            event = columns[2].get_text()
            location = columns[3].get_text()
            
            print(f"Date: {date}\nTime: {time}\nEvent: {event}\nLocation: {location}\n")
    else:
        print("No schedule table found on the page.")
else:
    print("Failed to retrieve the page.")