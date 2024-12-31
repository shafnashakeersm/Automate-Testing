from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome()

try:
    driver.get("https://www.flipkart.com/")
    time.sleep(5)
    nameTextBox=driver.find_element(By.NAME,"q")
    nameTextBox.send_keys("laptop")
    
    nameTextBox.send_keys(Keys.ENTER)  # to click enter the selected item
    time.sleep(5)

finally:
    driver.quit()