import time 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager


# start by defining the options 
options = webdriver.ChromeOptions() 
options.add_argument('--headless') 
options.page_load_strategy = 'none' 

chrome_service = Service(ChromeDriverManager().install() ) 
driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(5)

url = "https://www.usab.com/teams/5x5-mens-world-cup/schedules" 
driver.get(url) 
time.sleep(10)

try:
    content = driver.find_elements(By.CSS_SELECTOR, "time[class*='uppercase']")
    print(content.text)
finally:
    driver.quit()