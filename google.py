from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    time.sleep(3)
    check_element = driver.find_element(By.ID, "hplogo")
    check_element.click()
    time.sleep(5)
    

finally:
    driver.quit()