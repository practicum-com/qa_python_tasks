from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Find elements
email = driver...
password = driver...

# Test the placeholder attribute for each element
assert ...
assert ...

# Close the browser
driver...
