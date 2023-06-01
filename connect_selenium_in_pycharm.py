from selenium import webdriver
import time

# Initialize the driver
driver = webdriver.Chrome()

# Add a wait
time.sleep(5)

# Close the browser
driver.quit()
