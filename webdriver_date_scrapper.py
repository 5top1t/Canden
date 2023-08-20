import time 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Create Chrome options with headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Enable headless mode
driver = webdriver.Chrome(options=chrome_options)

try:
    url = "https://www.usab.com/teams/5x5-mens-world-cup/schedules" 
    driver.get(url) 
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the element containing the game schedule
    schedule_list = soup.find_all('div', class_='font-title')
    # print("Schedule list", schedule_list)

    if schedule_list:
        # Extract information from the table rows
        for date_entry in schedule_list:
            # print(date_entry)
            month_time = date_entry.find('time', class_='uppercase').get_text()
            day_text = date_entry.find('time', class_='days').get_text()
            
            # Events in the past have no time element
            time_element = date_entry.find('span', class_='uppercase')
            time_text = time_element.get_text() if time_element else ""
            
            print(f"Month: {month_time}\nDay: {day_text}\nTime: {time_text}\n")
    else:
        print("No schedule table found on the page.")
finally:
    driver.quit()