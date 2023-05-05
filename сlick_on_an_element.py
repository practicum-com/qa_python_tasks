from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://around.en.practicum-services.com/")

# Найди кнопку и кликни по ней
driver.find_element(...)...

driver.quit()
