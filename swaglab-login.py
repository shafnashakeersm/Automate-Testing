from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/v1/")
    time.sleep(1)

    nameTextBox=driver.find_element(By.ID,"user-name")
    nameTextBox.send_keys("standard_user")
    nameTextBox=driver.find_element(By.ID,"password")
    nameTextBox.send_keys("secret_sauce")
    time.sleep(1)
    nameTextBox=driver.find_element(By.ID,"login-button")
    nameTextBox.click()
    time.sleep(3)

    actualTitle=driver.title
    if actualTitle=="Swag Labs":
        print("PASSED")
        driver.back()
    else:
        print("FAILED")


    nameTextBox=driver.find_element(By.ID,"user-name")
    nameTextBox.send_keys("admi")
    nameTextBox=driver.find_element(By.ID,"password")
    nameTextBox.send_keys(1234)
    time.sleep(1)
    nameTextBox=driver.find_element(By.ID,"login-button")
    nameTextBox.click()
    time.sleep(3)

    
    if actualTitle=="Swag Labs":
        print("PASSED")
        
    else:
        print("FAILED")


finally:
    driver.quit()