from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

try:
    driver.get("https://www.demoblaze.com/#")
    time.sleep(1)
   
   

    #cart
    nameTextBox=driver.find_element(By.ID,"itemc")
    nameTextBox.click()
    time.sleep(1)

   

    actualTitle=driver.title
    if actualTitle=="STORE":
        print("PASSED")
    else:
        print("FAILED")

finally:
    driver.quit()