from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import pymongo

# MongoDB Configuration
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['twitter_trends']
collection = db['trends']

# Configure Proxy (IP Address)
PROXY = "45.127.56.194:8080"  # Replace with your provided IP address

def get_driver():
    options = Options()
    options.add_argument(f"--proxy-server=http://{PROXY}")
    options.add_argument("--headless")  # Run in headless mode for efficiency
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_twitter():
    driver = get_driver()
    try:
        # Open Twitter login page
        driver.get("https://twitter.com/login")
        
        # Perform login
        username_field = driver.find_element(By.NAME, "text")
        username_field.send_keys("PulateNile62101")
        driver.find_element(By.XPATH, '//span[text()="Next"]').click()
        
        driver.implicitly_wait(5)  # Wait for the password field to load
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("KRP8767542209")
        driver.find_element(By.XPATH, '//span[text()="Log in"]').click()
        
        # Scrape trending topics
        driver.implicitly_wait(10)  # Wait for the homepage to load
        trends = driver.find_elements(By.XPATH, '//section//span')[:5]
        trend_names = [trend.text for trend in trends if trend.text]

        # Store data in MongoDB
        unique_id = str(datetime.now().timestamp())
        record = {
            "_id": unique_id,
            "trend1": trend_names[0],
            "trend2": trend_names[1],
            "trend3": trend_names[2],
            "trend4": trend_names[3],
            "trend5": trend_names[4],
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ip_address": PROXY
        }
        collection.insert_one(record)
        
        return record
    finally:
        driver.quit()

if __name__ == "__main__":
    print(scrape_twitter())
