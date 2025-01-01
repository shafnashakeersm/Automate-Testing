from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

try:
    driver.get("https://www.alameencollege.org/")
    time.sleep(1)
   

    nameTextBox=driver.find_element(By.ROLE,"button")
    nameTextBox.click()
    time.sleep(1)

    nameTextBox=driver.find_element(By.ID,"menu-item-dropdown-4059")
    nameTextBox.click()
    time.sleep(1)

    nameTextBox=driver.find_element(By.ID,"menu-item-dropdown-4144")
    nameTextBox.click()
    time.sleep(1)

    actualTitle=driver.title
    if actualTitle=="Computer Applications | FISAT | Federal Institute of Science And Technology":
        print("PASSED")
    else:
        print("FAILED")

finally:
    driver.quit()