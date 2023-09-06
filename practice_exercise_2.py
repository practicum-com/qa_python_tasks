import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://around-v1.nm.tripleten-services.com/signin?lng=en")

# Log in
...

# Add an explicit wait for the page to load
...

# Save the title of the most recent card
title_before = ...

# Click on the button that posts a new card
driver.find_element(...)...

# Generate the new name of the place and enter it in the Name field
new_title = ...
driver.find_element(...)...

# Insert link to the picture in the Link field
driver.find_element(...)...

# Save the data
driver.find_element(...)...

# Wait for the Delete button to appear
WebDriverWait(...).until(...)

# Check that the card has the correct title
title_after = ...
assert ...

# Save the number of cards before deleting
cards_before = len(...)

# Delete the card
driver.find_element(...)...

# Wait for the title of the most recent card to become equal to title_before
WebDriverWait(...).until(...)

# Check that there is one less card now 
cards_after = len(...)
assert ...

driver.quit()
