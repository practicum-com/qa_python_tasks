from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Find the Email field and fill it in
driver.find_element(...)...

# Find the Password field and fill it in
driver.find_element(...)...

# Find the Login button and click on it
driver.find_element(...)...

# Add an explicit wait for the page to load
WebDriverWait(driver, 3)...

# Check that the current URL is 'https://around-v1.nm.tripleten-services.com/signin?lng=en'
...

driver.quit()
