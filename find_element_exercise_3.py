from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.en.practicum-services.com/")

# Find elements
email = driver...
password = driver...

# Test the placeholder attribute for each element
assert ...
assert ...

# Close the browser
driver...
