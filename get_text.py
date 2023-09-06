from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Find the Email field and fill it in
...

# Find the Password field and fill it in
...

# Find the Login button and click on it
...

# Add an explicit wait for the page to load
WebDriverWait(...).until(...)

# Find the button, retrieve its text, and check that the text value is 'Logout'
assert ...

driver.quit()
