from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.youtube.com/")
    time.sleep(1)
    check_element = driver.find_element(By.NAME, "search_query")
    check_element.send_keys("oru vezham")
    time.sleep(2)
    check_element.send_keys(Keys.ENTER)
    time.sleep(5)

finally:
    driver.quit() 