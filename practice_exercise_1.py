from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.en.practicum-services.com/")

# Log in
...

# Add an explicit wait for the feed to load
...

# Click on the profile picture
driver.find_element(...)...

# Insert the link to the picture in the Link field, using the avatar_url variable
avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"
driver.find_element(...)....

# Save the new picture
driver.find_element(...)...

# Save the value of the style attribute for the profile picture element to the style variable
style = driver.find_element(...)...
# Check that style contains the link to the profile picture
assert ...

driver.quit()
