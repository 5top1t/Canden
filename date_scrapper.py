import requests
from bs4 import BeautifulSoup

url = "https://www.usab.com/teams/5x5-mens-world-cup/schedules"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the element containing the game schedule
    schedule_list = soup.find('div', class_='font-title')
    print("Schedule list", schedule_list)
    
    if  schedule_list:
        # Extract information from the table rows
        for date_entry in schedule_list: 
            month = date_entry.find('time', class_='uppercase').get_text()
            day = date_entry.find('time', class_='days').get_text()
            time = date_entry.find('span', class_='uppercase').get_text()
            
            print(f"Month: {month}\nDay: {day}\nTime: {time}\n")
    else:
        print("No schedule table found on the page.")
else:
    print("Failed to retrieve the page.")