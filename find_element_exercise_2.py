from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Find all elements
elements = driver...

# Check that the number of elements found is greater than 1 by using len()
...

# Close the browser
driver...
