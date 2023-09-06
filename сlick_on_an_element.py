from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Find the button and click on it
driver.find_element(...)...

driver.quit()
