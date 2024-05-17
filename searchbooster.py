from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import schedule
import time

def run_selenium_script():
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    now = datetime.now()

    formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    driver.get("https://www.google.com")

    WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )

    input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
    input_element.clear()
    input_element.send_keys("lans san francisco" + Keys.ENTER)

    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "lans"))
    )

    link = driver.find_element(By.PARTIAL_LINK_TEXT, "lans")
    link.click()

    WebDriverWait(driver,15).until(
        EC.presence_of_element_located((By.CLASS_NAME, "text-field-3"))
    )

    input_element = driver.find_element(By.CLASS_NAME, "text-field-3")
    input_element.clear()
    input_element.send_keys("FurkanBot was here")

    input_element = driver.find_element(By.CLASS_NAME, "text-field-2")
    input_element.clear()
    input_element.send_keys("FurkanBot13231313@gmail.com")

    input_element = driver.find_element(By.ID, "Form-Area")
    input_element.clear()
    input_element.send_keys("FurkaBot submitted the form successfully at " + formatted_date_time)

    # Locate and click the button with value "SEND"
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="SEND"]'))
    )
    send_button.click()

    time.sleep(10)
    driver.quit()

# Schedule the script to run at 10 AM, 4 PM, and 8 PM
schedule.every().day.at("13:36").do(run_selenium_script)
schedule.every().day.at("16:00").do(run_selenium_script)
schedule.every().day.at("20:00").do(run_selenium_script)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
