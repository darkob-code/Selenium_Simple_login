from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

user = "Selenium"
passw = "Se123456"

url = "https://www.stealmylogin.com/demo.html"

os.environ['PATH'] += "c:\Selenium_Driver"
driver = webdriver.Chrome()

driver.get(url)

driver.find_element(By.NAME, 'username').send_keys(user)
driver.find_element(By.NAME, 'password').send_keys(passw)
driver.find_element(By.CSS_SELECTOR, 'input[type=\"submit\" i]').click()

print("login ok")